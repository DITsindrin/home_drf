# Generated by Django 4.2.7 on 2024-02-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0006_alter_lesson_owner_alter_trainingcourse_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video_url',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ссылка на видео'),
        ),
    ]
