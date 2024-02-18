from django.contrib import admin

from materials.models import Lesson, TrainingCourse


# Register your models here.
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    fields = ('title', 'preview', 'description', 'video_url', 'owner', 'course')


@admin.register(TrainingCourse)
class TrainingCourseAdmin(admin.ModelAdmin):
    fields = ('title', 'preview', 'description', 'owner',)
