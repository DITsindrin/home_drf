# Generated by Django 4.2.7 on 2024-02-09 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_alter_lesson_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='preview',
            field=models.ImageField(default='lesson.png', upload_to='materials/lesson/', verbose_name='Превью'),
        ),
    ]
