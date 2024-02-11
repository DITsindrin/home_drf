# Generated by Django 4.2.7 on 2024-02-11 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_alter_lesson_course'),
        ('users', '0002_rename_city_user_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_payment', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата оплаты')),
                ('payment_amount', models.IntegerField(verbose_name='сумма оплаты')),
                ('payment_method', models.CharField(choices=[('cash', 'наличными'), ('card', 'картой')], max_length=35, verbose_name='способ оплаты')),
                ('paid_course', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.trainingcourse', verbose_name='оплаченный курс')),
                ('paid_lesson', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.lesson', verbose_name='оплаченный урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
            },
        ),
    ]