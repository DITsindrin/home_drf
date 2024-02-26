from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import TrainingCourse, Lesson, Subscription
from materials.validators import LessonVideoUrlValidator


class SubscriptionSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Подписки """
    signed = SerializerMethodField()

    def get_signed(self, obj):
        """ Метод отображения признака подписки пользователю """
        subs = Subscription.objects.filter(course=obj.pk)

        for sub in subs:
            for user in obj.user.all():
                if sub.user == user:
                    return True

        return False

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
    subscription = SubscriptionSerializer(many=True, read_only=True)

    def get_lesson_count(self, instance):
        if instance.lesson.all():
            lesson_count = instance.lesson.all().count()
            return lesson_count
        return 0

    class Meta:
        model = TrainingCourse
        fields = '__all__'
