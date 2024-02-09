from rest_framework import serializers

from materials.models import TrainingCourse, Lesson


class TrainingCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrainingCourse
        fields = ('title', 'description',)


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('title', 'description', 'video_url', 'course',)
