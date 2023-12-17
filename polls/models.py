import datetime
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, FileExtensionValidator
from django.db import models
from django.dispatch import Signal
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string


def get_name_file(instance, filename):
    return 'mysite/file'.join([get_random_string(5) + '_' + filename])


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='Название опроса')
    pub_date = models.DateTimeField('date published')
    description_question = models.CharField(max_length=200, verbose_name='Краткое описание')
    description_choice = models.CharField(max_length=200, verbose_name='Подробное описание')
    img = models.ImageField(verbose_name='Картинка', upload_to=get_name_file, blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, validators=[
        RegexValidator(), ])
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    voter = models.ForeignKey('User', verbose_name='Пользователь', related_name='+', on_delete=models.CASCADE)
    question_vote = models.ForeignKey(Question, verbose_name='Опрос', on_delete=models.CASCADE)


class User(AbstractUser):
    username = models.CharField(max_length=200, verbose_name='Логин', unique=True, blank=False, validators=[
        RegexValidator(
            regex='^[A-Za-z -]*$',
            message='Имя пользователя должно состоять только из латиницы',
            code='invalid_username'
        ),
    ])
    avatar = models.ImageField(upload_to=get_name_file, verbose_name='Аватар', blank=False, null=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    password = models.CharField(max_length=200, verbose_name='Пароль', blank=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.username)


user_registrated = Signal()
