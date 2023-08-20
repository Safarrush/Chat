from django.db import models
from django.contrib.auth.models import AbstractUser

from .validators import validate_username
from django.contrib.auth.models import AbstractUser, BaseUserManager

MAX_LENGTH = 254

 
class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not email: 
            raise ValueError("Вы не ввели Email")
        if not username:
            raise ValueError("Вы не ввели Логин")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, username, password):
        return self._create_user(email, username, password)
 
    def create_superuser(self, email, username, password):
        return self._create_user(email, username, password, is_staff=True, is_superuser=True)


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

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username