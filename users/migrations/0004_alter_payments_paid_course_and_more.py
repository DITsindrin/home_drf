# Generated by Django 4.2.7 on 2024-02-18 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_alter_lesson_course'),
        ('users', '0003_payments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='paid_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.trainingcourse', verbose_name='оплаченный курс'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='paid_lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.lesson', verbose_name='оплаченный урок'),
        ),
    ]