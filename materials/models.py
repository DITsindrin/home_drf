from django.db import models


# Create your models here.

class TrainingCourse(models.Model):
    """" Модель Курсов """
    title = models.CharField(max_length=150, verbose_name='Название курса')
    preview = models.ImageField(upload_to='materials/course/', default='course.png', verbose_name='Превью')
    description = models.TextField(verbose_name='Описание курса')
    last_update = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='последнее обновление')

    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, verbose_name='Владелец', null=True)
    price = models.PositiveIntegerField(default=10000, verbose_name='Цена курса')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """" Модель Уроков """
    title = models.CharField(max_length=150, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса')
    preview = models.ImageField(upload_to='materials/lesson/', default='lesson.png', verbose_name='Превью')
    video_url = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Ссылка на видео')

    course = models.ForeignKey(TrainingCourse, on_delete=models.CASCADE, verbose_name='Курс', related_name='lesson')
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, verbose_name='Владелец', null=True)
    price = models.PositiveIntegerField(default=1000, verbose_name='Цена урока')

    def __str__(self):
        return f'{self.title} {self.description} {self.course}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Subscription(models.Model):
    """ Модель пописки """
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(TrainingCourse, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f'{self.user}-{self.course}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
