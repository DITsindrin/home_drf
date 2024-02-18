from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny

from users.models import User, Payments
from users.serializers import UserSerializer, UserRegisterSerializer, UserListSerializer, PaymentsSerializer, \
    UserPublicRetrieveSerializer


# Create your views here.

# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()


class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserPublicRetrieveSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.user == super().get_object():
            self.serializer_class = UserSerializer
            return self.serializer_class
        return UserPublicRetrieveSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_update(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)
    ordering_fields = ('date_payment',)
