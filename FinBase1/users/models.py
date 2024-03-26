from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    """
    Custom user model representing a user in the system.

    Attributes:
        username (CharField): The username for the user. Must be unique.
        first_name (CharField): The first name of the user.
        last_name (CharField): The last name of the user.
        country (CharField): The country of the user.
        city (CharField): The city of the user.
        street (CharField): The street of the user.
        phone (PositiveBigIntegerField): The phone number of the user.
        telegram_url (CharField): The Telegram URL of the user. Must start with "@" and contain only letters, digits,
                                and underscores.

    Meta:
        unique_together (list): Specifies that the combination of first_name and last_name must be unique.

    Methods:
        __str__: Returns a string representation of the user, concatenating the first name and last name.
    """
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
        """
        Returns a string representation of the user, concatenating the first name and last name.
        """
        return f'{self.first_name} {self.last_name}'
