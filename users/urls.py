from django.urls import path, include

from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, PaymentsListAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'', UserViewSet, basename='users')

urlpatterns = [
    path('payment/', PaymentsListAPIView.as_view(), name='payment-list'),
] + router.urls