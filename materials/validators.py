import re
from rest_framework.serializers import ValidationError


class LessonVideoUrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = 'youtube.com'
        tmp_val = dict(value).get(self.field)
        if reg in tmp_val:
            print('OK')
        else:
            raise ValidationError('Video_url is no ok')


