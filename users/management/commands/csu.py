from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Комманда для создания суперпользователя"""
    def handle(self, *args, **options):
        user = User.objects.create(
            email='dmitriytsindrin@mail.ru',
            first_name='Admin',
            last_name='MailingService',
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('019060')
        user.save()
