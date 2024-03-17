from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
       Сериализатор для пользователя.

       Поля:
       - id: Уникальный идентификатор пользователя (тип: целое число).
       - username: Имя пользователя (тип: строка).
       - first_name: Имя пользователя (тип: строка).
       - last_name: Фамилия пользователя (тип: строка).
       - country: Страна пользователя (тип: строка).
       - city: Город пользователя (тип: строка).
       - street: Улица пользователя (тип: строка).
       - phone: Номер телефона пользователя (тип: целое число).
       - telegram_url: URL профиля Telegram пользователя (тип: строка).
       - password: Пароль пользователя (тип: строка, доступен только для записи).

       Примечания:
       - Поле "password" доступно только для записи (write_only=True), и не включено в выходные данные по умолчанию.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'country', 'city', 'street', 'phone', 'telegram_url']
        extra_kwargs = {'password': {'write_only': True}}


class UserPassChangeSerializer(serializers.Serializer):
    """
        Сериализатор для изменения пароля пользователя.

        Поля:
        - old_pass: Старый пароль пользователя (тип: строка, обязательное поле).
        - new_pass: Новый пароль пользователя (тип: строка, обязательное поле).

        Примечания:
        - Оба поля обязательны для заполнения.
    """
    old_pass = serializers.CharField(required=True)
    new_pass = serializers.CharField(required=True)
