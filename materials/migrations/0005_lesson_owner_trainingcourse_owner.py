# Generated by Django 4.2.7 on 2024-02-18 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_alter_lesson_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='owner',
            field=models.CharField(max_length=75, null=True, verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='trainingcourse',
            name='owner',
            field=models.CharField(max_length=75, null=True, verbose_name='Владелец'),
        ),
    ]