from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import TrainingCourse, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('title', 'description', 'video_url', 'course',)


class TrainingCourseSerializer(serializers.ModelSerializer):
    lesson_count = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    def get_lesson_count(self, instance):
        if instance.lesson.all():
            lesson_count = instance.lesson.all().count()
            return lesson_count
        return 0

    class Meta:
        model = TrainingCourse
        fields = '__all__'
