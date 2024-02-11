from django.test import TestCase

# Create your tests here.
from models import TrainingCourse, Lesson

a = TrainingCourse.lesson_set.all()
print(a)