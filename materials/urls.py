from django.urls import path, include

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import TrainingCourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, SubscriptionView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'course', TrainingCourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-detail'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
    path('subscription/', SubscriptionView.as_view(), name='subscription'),

] + router.urls
