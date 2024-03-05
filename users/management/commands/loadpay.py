from django.core.management import BaseCommand

from materials.models import TrainingCourse, Lesson
from users.models import Payments, User

test_payments = [
    {
        "user_id": 1,
        "date": "2024-02-01",
        "course_id": 1,
        "payment_amount": 10000,
        "payment_method": "card",
    },
    {
        "user_id": 1,
        "date": "2024-02-02",
        "paid_course_id": 1,
        "payment_amount": 20000,
        "payment_method": "card",
    },
    {
        "user_id": 1,
        "date": "2024-02-03",
        "paid_lesson_id": 1,
        "payment_amount": 10000,
        "payment_method": "card",
    },
    {
        "user_id": 1,
        "date": "2024-02-04",
        "paid_lesson_id": 2,
        "payment_amount": 15000,
        "payment_method": "card",
    },
    {
        "user_id": 1,
        "date": "2024-02-05",
        "paid_lesson_id": 3,
        "payment_amount": 20000,
        "payment_method": "card",
    },
    {
        "user_id": 1,
        "date": "2024-02-06",
        "paid_lesson_id": 4,
        "payment_amount": 9000,
        "payment_method": "card",
    }
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for test_payment in test_payments:
            payment = Payments.objects.create(**test_payment)
            payment.save()
        print('Test payments were added in database')

# class Command(BaseCommand):
#     """Заполняет БД данными по платежам. при реальном наполнении можно читать json файл с платежами и формировать список \
#     объектов Payments для пакетного заполнения БД"""
#
#     lesson_queryset = Lesson.objects.all()
#     print(lesson_queryset)
#     course_queryset = TrainingCourse.objects.get(pk=1)
#     print(course_queryset)
#     user_queryset = User.objects.all()
#     print(user_queryset)
#
#     def handle(self, *args, **options):
#         # payments_list = [
#         #     {'payment_amount': 5600, 'payment_method': 'cash', 'user': self.user_queryset[0],
#         #      "paid_lesson": self.lesson_queryset[0]},
#         #     {'payment_amount': 5600, 'payment_method': 'cash', 'user': self.user_queryset[0],
#         #      "paid_lesson": self.lesson_queryset[1]},
#         #     {'payment_amount': 5600, 'payment_method': 'cash', 'user': self.user_queryset[0],
#         #      "paid_lesson": self.lesson_queryset[2]},
#         #     {'payment_amount': 25000, 'payment_method': 'card', 'user': self.user_queryset[1],
#         #      "paid_course": self.course_queryset},
#         #
#         # ]
#         payments_list = [
#             {
#                 'payment_amount': 25000, 'payment_method': 'card', 'user': {'email': 'test@mail.ru', 'password': 12345},
#                 'paid_course': {'title': 'Новый курс', 'description': 'Хороший курс'}
#             },
#             {
#                 'payment_amount': 5600, 'payment_method': 'cash', 'user': {'email': 'tset@mail.ru', 'password': 12345},
#                 'paid_lesson': {'title': 'Четвертый урок', 'description': 'Хороший урок',
#                                 'course': self.course_queryset}
#             },
#             {
#                 'payment_amount': 5600, 'payment_method': 'cash', 'user': {'email': 'tset@mail.ru', 'password': 12345},
#                 'paid_lesson': {'title': 'Четвертый урок', 'description': 'Хороший урок',
#                                 'course': self.course_queryset}
#             },
#             {
#                 'payment_amount': 5600, 'payment_method': 'cash', 'user': {'email': 'tset@mail.ru', 'password': 12345},
#                 'paid_lesson': {'title': 'Четвертый урок', 'description': 'Хороший урок',
#                                 'course': self.course_queryset}
#             },
#         ]
#
#         payments_for_create = []
#         for payment in payments_list:
#             payments_for_create.append(Payments(**payment))
#             print(payment)
#
#         print(payments_for_create)
#         Payments.objects.bulk_create(payments_for_create)
