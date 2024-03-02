from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import TrainingCourse, Lesson, Subscription
from materials.validators import LessonVideoUrlValidator


class SubscriptionSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Подписки """

    class Meta:
        model = Subscription
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Lesson"""

    class Meta:
        model = Lesson
        fields = ('title', 'description', 'video_url', 'course',)
        validators = [
            LessonVideoUrlValidator(field='video_url'),
        ]


class TrainingCourseSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели TrainingCourse"""
    lesson_count = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)
    signed_subscription = SerializerMethodField()

    def get_lesson_count(self, instance):
        if instance.lesson.all():
            lesson_count = instance.lesson.all().count()
            return lesson_count
        return 0

    def get_signed_subscription(self, instance):
        """ Метод отображения признака подписки пользователю """
        subscription = Subscription.objects.all().filter(course=instance.pk).filter(
            user=self.context.get('request').user.pk)

        if subscription:
            return True
        else:
            return False

    class Meta:
        model = TrainingCourse
        fields = '__all__'
