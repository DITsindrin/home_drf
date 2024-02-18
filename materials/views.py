from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from materials.models import TrainingCourse, Lesson
from materials.permissions import IsModer, IsOwner
from materials.serializers import TrainingCourseSerializer, LessonSerializer


# Create your views here.


class TrainingCourseViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingCourseSerializer
    queryset = TrainingCourse.objects.all()

    def perform_create(self, serializer):
        new_course = serializer.save(owner=self.request.user)
        new_course.save()

    def get_permissions(self):
        if self.action in ('create',):
            self.permission_classes = [IsAuthenticated, ~IsModer]
        elif self.action in ('destroy',):
            self.permission_classes = [IsAuthenticated, IsOwner]
        elif self.action in ('update', 'retrieve',):
            self.permission_classes = [IsAuthenticated, IsModer | IsOwner]

        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModer]

    def perform_create(self, serializer):
        new_lesson = serializer.save(owner=self.request.user)
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsOwner]

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
