from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from users.models import User, Payments


class PaymentsSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Payments"""
    class Meta:
        model = Payments
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели User c полем платежи"""
    payment = PaymentsSerializer(source='payments_set', many=True)

    class Meta:
        model = User
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    """Сериалайзер для регистрации объекта модели User"""
    class Meta:
        model = User
        fields = ('email', 'password',)


class UserListSerializer(serializers.ModelSerializer):
    """Сериалайзер для вывода списка объектов модели User с нужными полями"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)


class UserPublicRetrieveSerializer(serializers.ModelSerializer):
    """Сериалайзер для публичного просмотра объекта модели User другими объектами модели User"""
    class Meta:
        model = User
        fields = ('first_name', 'phone', 'email', 'city', 'avatar', )
