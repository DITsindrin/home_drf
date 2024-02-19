from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from materials.models import TrainingCourse, Lesson
from materials.permissions import IsModer, IsOwner
from materials.serializers import TrainingCourseSerializer, LessonSerializer


# Create your views here.


class TrainingCourseViewSet(viewsets.ModelViewSet):
    """CRUD для объектов модели TrainingCourse """
    serializer_class = TrainingCourseSerializer
    queryset = TrainingCourse.objects.all()

    def perform_create(self, serializer):
        """Метод для записи поля owner при создании объекта TrainingCourse"""
        new_course = serializer.save(owner=self.request.user)
        new_course.save()

    def get_permissions(self):
        """Метод для описания прав по созданию, удалению, изменению и просмотру объектов модели TrainingCourse"""
        if self.action in ('create',):
            self.permission_classes = [IsAuthenticated, ~IsModer]
        elif self.action in ('destroy',):
            self.permission_classes = [IsAuthenticated, IsOwner]
        elif self.action in ('update', 'retrieve',):
            self.permission_classes = [IsAuthenticated, IsModer | IsOwner]

        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    """Вывод списка объектов модели Lesson """
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModer]

    def perform_create(self, serializer):
        """Метод для записи поля owner при создании объекта Lesson"""
        new_lesson = serializer.save(owner=self.request.user)
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """Вывод списка объектов модели Lesson """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsOwner]

    def get_queryset(self):
        """Метод для фильтрации списка выводимых уроков по полю owner"""
        return super().get_queryset().filter(owner=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Вывод детальной информации об объекте модели Lesson """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Изменение объекта модели Lesson """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Удаление объекта модели Lesson """
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
