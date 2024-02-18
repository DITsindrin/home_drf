from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from users.models import User, Payments


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    payment = PaymentsSerializer(source='payments_set', many=True)

    class Meta:
        model = User
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password',)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)


class UserPublicRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'phone', 'email', 'city', 'avatar', )
