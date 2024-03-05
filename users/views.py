from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny

from users.models import User, Payments
from users.serializers import UserSerializer, UserRegisterSerializer, UserListSerializer, PaymentsSerializer, \
    UserPublicRetrieveSerializer, PaymentsCreateSerializer
from users.services import create_stripe_product, create_stripe_price, create_stripe_session


# Create your views here.

# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()


class UserRegisterAPIView(generics.CreateAPIView):
    """Создание объекта модели User"""
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """Активавация пользователя и Шифровка поля password"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """Вывод списка объектов модели User"""
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Детальный просмотр информации об объекте модели User"""
    serializer_class = UserPublicRetrieveSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        """Метод выбора сериолайзера в зависимости от условий"""
        if self.request.user == super().get_object():
            self.serializer_class = UserSerializer
            return self.serializer_class

        self.serializer_class = UserPublicRetrieveSerializer
        return self.serializer_class


class UserUpdateAPIView(generics.UpdateAPIView):
    """Изменение объекта модели User"""
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_update(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserDeleteView(generics.DestroyAPIView):
    """Удаление объекта модели User"""
    queryset = User.objects.all()


class PaymentsListAPIView(generics.ListAPIView):
    """Вывод всех объектов модели Payments"""
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)
    ordering_fields = ('date_payment',)


class PaymentsCreateAPIView(generics.CreateAPIView):
    """Вывод всех объектов модели Payments"""
    serializer_class = PaymentsCreateSerializer

    def perform_create(self, serializer):
        a = serializer.validated_data
        print(a)
        # course = serializer.validated_data['paid_course']
        # lesson = serializer.validated_data['paid_lesson']
        payment_method = 'card'
        if serializer.validated_data['paid_course']:
            course = serializer.validated_data['paid_course']
            stripe_product_id = create_stripe_product(course.title)
            stripe_price_id = create_stripe_price(course.price, stripe_product_id)
            payment_amount = course.price
        elif serializer.validated_data['paid_lesson']:
            lesson = serializer.validated_data['paid_lesson']
            stripe_product_id = create_stripe_product(lesson.title)
            stripe_price_id = create_stripe_price(lesson.price, stripe_product_id)
            payment_amount = lesson.price

        url_for_payment, payment_id = create_stripe_session(stripe_price_id)
        if course:
            serializer.save(payment_amount=payment_amount, url_for_payment=url_for_payment, payment_id=payment_id,
                            paid_course=course, user=self.request.user, payment_method=payment_method,
                            product_stripe_id=stripe_product_id)  # расширить модель
        elif lesson:
            serializer.save(payment_amount=payment_amount, url_for_payment=url_for_payment, payment_id=payment_id,
                            paid_lesson=lesson, user=self.request.user, payment_method=payment_method,
                            product_stripe_id=stripe_product_id)
