from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    is_active = models.BooleanField(default=False, verbose_name='Признак верификации')

    phone = models.CharField(max_length=50, blank=True, null=True, verbose_name='Телефон')
    City = models.CharField(max_length=75, blank=True, null=True, verbose_name='Город')
    avatar = models.ImageField(upload_to='users/', default='users.png', verbose_name='Аватар')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
