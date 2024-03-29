from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from materials.models import TrainingCourse, Lesson


# Create your models here.

class User(AbstractUser):
    """"Модель пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    is_active = models.BooleanField(default=False, verbose_name='Признак верификации')

    phone = models.CharField(max_length=50, blank=True, null=True, verbose_name='Телефон')
    city = models.CharField(max_length=75, blank=True, null=True, verbose_name='Город')
    avatar = models.ImageField(upload_to='users/', default='users.png', verbose_name='Аватар')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payments(models.Model):
    """"Модель платежи"""
    date_payment = models.DateTimeField(default=timezone.now, verbose_name='Дата оплаты')
    payment_amount = models.IntegerField(verbose_name='Сумма оплаты', null=True, blank=True)
    payment_method = models.CharField(max_length=35, choices=(('cash', 'наличными'), ('card', 'картой')),
                                      verbose_name='Способ оплаты')

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='пользователь')
    paid_course = models.ForeignKey(TrainingCourse, on_delete=models.CASCADE, null=True, blank=True,
                                    verbose_name='Оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True,
                                    verbose_name='Оплаченный урок')
    url_for_payment = models.URLField(max_length=500, null=True, blank=True, verbose_name='Ссылка для оплаты')
    payment_id = models.CharField(max_length=250, null=True, blank=True, verbose_name='id сессии оплаты')
    product_stripe_id = models.CharField(max_length=250, null=True, blank=True, verbose_name='id продукта stripe')

    def __str__(self):
        return f'{self.user} {self.paid_course if self.paid_course else self.paid_lesson} - {self.date_payment} {self.payment_amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
