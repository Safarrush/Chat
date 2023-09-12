from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from .validators import validate_username

USER = settings.AUTH_USER_MODEL
MAX_LENGTH = 254


class User(AbstractUser):
    username = models.CharField(
        blank=True,
        max_length=150,
        unique=True,
        validators=[validate_username],
        verbose_name='Уникальный юзернейм',
        help_text='Имя пользователя'
    )
    email = models.EmailField(
        verbose_name="Email",
        max_length=MAX_LENGTH,
        unique=True,
        help_text='Адрес электронной почты'
    )
    first_name = models.CharField(max_length=150,)
    last_name = models.CharField(max_length=150,)

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    loction = models.CharField(max_length=220, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
