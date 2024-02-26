from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from materials.models import Lesson, Subscription, TrainingCourse
from users.models import User


class LessonCreateTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        self.user = User.objects.create(
            email='TestCreate@mail.ru',
            password='12345678',
            is_superuser=True,
            is_staff=True
        )
        print(self.user)

        self.client.force_authenticate(user=self.user)

        self.course = TrainingCourse.objects.create(
            title='TestCreate',
            description='TestCreate',
            owner=self.user
        )
        print(self.course)

    def test_lesson_create(self):
        data = {
            'title': 'TestCreate',
            'description': 'TestCreate',
            'video_url': 'https://www.youtube.com/',
            'course': {self.course.id},
            'owner': {self.user.id}
        }
        response = self.client.post(
            '/lesson/create/',
            data=data
        )
        print(response.json)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )


class LessonListTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()

        self.user = User.objects.create(
            email='TestList@mail.ru',
            password='12345678',
            is_superuser=True,
            is_staff=True
        )
        print(self.user)

        self.client.force_authenticate(user=self.user)

        self.course = TrainingCourse.objects.create(
            title='TestListC',
            description='TestListC',
            owner=self.user
        )
        print(self.course)

        self.lesson = Lesson.objects.create(
            title='TestListL',
            description='TestListL',
            video_url='https://www.youtube.com/',
            course=self.course,
            owner=self.user
        )
        print(self.lesson)

    def test_lesson_list(self):
        response = self.client.get(
            '/lesson/'
        )
        print(response.json)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class LessonDetailTestCase(APITestCase):
    pass


class LessonUpdateTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        self.user = User.objects.create(
            email='TestUpdate@mail.ru',
            password='12345678',
            is_superuser=True,
            is_staff=True
        )
        print(self.user)

        self.client.force_authenticate(user=self.user)

        self.course = TrainingCourse.objects.create(
            title='TestUpdate',
            description='TestUpdate',
            owner=self.user
        )
        print(self.course)

        self.lesson = Lesson.objects.create(
            title='TestUpdate',
            description='TestListL',
            video_url='https://www.youtube.com/',
            course=self.course,
            owner=self.user
        )
        print(self.lesson)

    def test_lesson_update(self):
        new_description = 'TestUpdate'
        data = {
            'title': 'TestUpdate',
            'description': new_description,
            'video_url': {self.lesson.video_url},
            'course': {self.course.id},
            'owner': {self.user.id}
        }
        print(self.lesson.id)
        print(self.lesson.video_url)
        print(self.user.email)
        print(self.lesson.owner)

        response = self.client.put(
            f'/lesson/update/{self.lesson.id}/',
            data=data
        )
        print(response.json)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class LessonDeleteTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        self.user = User.objects.create(
            email='TestDelete@mail.ru',
            password='12345678',
            is_superuser=True,
            is_staff=True
        )
        print(self.user)

        self.client.force_authenticate(user=self.user)

        self.course = TrainingCourse.objects.create(
            title='TestDelete',
            description='TestDelete',
            owner=self.user
        )
        print(self.course)

        self.lesson = Lesson.objects.create(
            title='TestDelete',
            description='TestDelete',
            video_url='https://www.youtube.com/',
            course=self.course,
            owner=self.user
        )
        print(self.lesson)

    def test_lesson_delete(self):
        print(self.lesson.id)

        response = self.client.delete(
            f'/lesson/delete/{self.lesson.id}/'
        )
        print(response.json)
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(
            email="Test@mail.ru",
            password='12345678',
            is_superuser=True,
            is_staff=True
        )
        self.client.force_authenticate(user=self.user)

        self.course = TrainingCourse.objects.create(
            title='Test',
            description='Test',
            owner=self.user
        )

    def test_retrieve_subscribe(self):
        """ Тестирование функционала работы подписки на обновления курса"""
        print(self.user.id)
        print(self.course.id)

        data = {
            "user": self.course.id,
            "course": self.user.id
        }

        response = self.client.post(
            '/subscription/',
            data=data
        )
        print(response.json)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
