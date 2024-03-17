from rest_framework import serializers
from .models import Ticket, User


class UserSerializer(serializers.ModelSerializer):
    """
        Сериализатор для пользователя.

        Поля:
        - id: Уникальный идентификатор пользователя (тип: целое число).
        - first_name: Имя пользователя (тип: строка).
        - last_name: Фамилия пользователя (тип: строка).
    """
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class TicketSerializer(serializers.ModelSerializer):
    """
        Сериализатор для билета.

        Поля:
        - event: Событие, на которое приобретен билет (тип: целое число, обязательное поле).
        - owner: Владелец билета (тип: объект пользователя, заполняется автоматически).
        - price: Цена билета (тип: десятичное число).
        - num_tickets: Количество билетов (тип: целое число).
        - purchase_date: Дата покупки билета (тип: дата).
        - timestamp: Временная метка создания билета (тип: дата и время, только для чтения).

        Примечания:
        - Поле "owner" автоматически заполняется текущим пользователем, который выполнил запрос на создание билета.
    """
    class Meta:
        model = Ticket
        fields = ['event', 'owner', 'price', 'num_tickets', 'purchase_date', 'timestamp']

    def create(self, validated_data):
        """
            Метод для создания нового билета.

            Параметры:
            - validated_data: Словарь с данными для создания билета.

            Возвращает:
            - Созданный объект билета.
        """
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
