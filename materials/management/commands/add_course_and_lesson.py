from django.core.management import BaseCommand

from materials.models import Lesson, TrainingCourse

test_course = {
    "title": "Course 1 Test",
    'description': "Test description for course 1",
    "owner_id": 1
}

test_lessons = [
    {
        "user_id": 1,
        "title": "Lesson 1",
        "description": "Decsription for lesson 1",
        "video_url": "www.testlink1.com",
        "owner_id": 1,
        "course_id": 1,
    },
    {
        "user_id": 1,
        "title": "Lesson 2",
        "description": "Decsription for lesson 2",
        "video_url": "www.testlink2.com",
        "owner_id": 1,
        "course_id": 1,
    },
    {
        "user_id": 1,
        "title": "Lesson 3",
        "description": "Decsription for lesson 3",
        "video_url": "www.testlink3.com",
        "owner_id": 1,
        "course_id": 1,
    },
    {
        "user_id": 1,
        "title": "Lesson 4",
        "description": "Decsription for lesson 4",
        "video_url": "www.testlink4.com",
        "owner_id": 1,
        "course_id": 1,
    },
    {
        "user_id": 1,
        "title": "Lesson 5",
        "description": "Decsription for lesson 5",
        "video_url": "www.testlink5.com",
        "owner_id": 1,
        "course_id": 1,
    },
    {
        "user_id": 1,
        "title": "Lesson 6",
        "description": "Decsription for lesson 6",
        "video_url": "www.testlink6.com",
        "owner_id": 1,
        "course_id": 1,
    },
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        course = TrainingCourse.objects.create(**test_course)
        course.save()
        for test_lesson in test_lessons:
            lesson = Lesson.objects.create(**test_lesson)
            lesson.save()
        print('Test lessons were added in database')
