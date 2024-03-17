from rest_framework import serializers

from .models import Event
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
        Сериализатор для пользователя.

        Поля:
        - id: Уникальный идентификатор пользователя (тип: целое число).
        - first_name: Имя пользователя (тип: строка).
        - last_name: Фамилия пользователя (тип: строка).

        Примечания:
        - Поле "id" автоматически генерируется и доступно только для чтения.
    """
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class EventSerializer(serializers.ModelSerializer):
    """
       Сериализатор для события.

       Поля:
       - attendees_count: Количество участников события (тип: целое число, доступно только для чтения).
       - organizer: Организатор события (тип: объект пользователя, сериализуемый с помощью UserSerializer).
       - title: Заголовок события (тип: строка).
       - description: Описание события (тип: строка).
       - date: Дата события (тип: дата).
       - location: Место проведения события (тип: строка).
       - category: Категория события (тип: строка).
       - capacity: Вместимость события (тип: целое число).
       - bookings: Количество бронирований на событие (тип: целое число).

       Примечания:
       - Поле "attendees_count" рассчитывается с помощью метода get_attendees_count и доступно только для чтения.
    """
    organizer = UserSerializer
    attendees_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['attendees_count', 'organizer', 'title', 'description', 'date', 'location', 'category',
                  'capacity', 'bookings']

    def get_attendees_count(self, obj):
        """
            Метод для получения количества участников события.

            Возвращает количество записей в связанном поле attendees модели Event.

            Параметры:
            - obj: Экземпляр объекта события.

            Возвращает:
            - Количество участников события (тип: целое число).
        """
        return obj.attendees.count()
