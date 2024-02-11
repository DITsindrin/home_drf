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
