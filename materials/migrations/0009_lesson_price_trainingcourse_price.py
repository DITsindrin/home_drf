# Generated by Django 4.2.7 on 2024-03-03 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0008_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='price',
            field=models.PositiveIntegerField(default=1000, verbose_name='Цена урока'),
        ),
        migrations.AddField(
            model_name='trainingcourse',
            name='price',
            field=models.PositiveIntegerField(default=10000, verbose_name='Цена курса'),
        ),
    ]
