from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30, default='')
    city = models.CharField(max_length=30, default='')
    street = models.CharField(max_length=30)
    phone = models.PositiveBigIntegerField(null=True)
    telegram_url = models.CharField(
        max_length=32, validators=[RegexValidator(
            regex='^@[\w\d_]*$', message='Telegram URL должен начинаться'
                                         ' с символа "@" и содержать только буквы,'
                                         ' цифры и символ "_"')])

    class Meta:
        unique_together = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
