from django.urls import path, include
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter

from users.views import PaymentsListAPIView, UserRegisterAPIView, UserListAPIView, UserRetrieveAPIView, \
    UserUpdateAPIView, UserDeleteView, PaymentsCreateAPIView

app_name = UsersConfig.name

# router = DefaultRouter()
# router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    # token
    path('token/', TokenObtainPairView.as_view(permission_classes=[AllowAny]), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=[AllowAny]), name='token_refresh'),

    # users
    path('', UserListAPIView.as_view(), name='user-list'),
    path('create/', UserRegisterAPIView.as_view(), name='user-create'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user-detail'),
    path('update/<int:pk>', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>', UserDeleteView.as_view(), name='user-delete'),
    path('payment/', PaymentsListAPIView.as_view(), name='payment-list'),
    path('payment/create/', PaymentsCreateAPIView.as_view(), name='payment-create'),
]
