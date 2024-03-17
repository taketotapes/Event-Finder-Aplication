from rest_framework import serializers
from events.serializers import EventSerializer
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отзывов.

    Поля:
    - id: Уникальный идентификатор отзыва (тип: целое число).
    - event: Связанное с отзывом событие (тип: целое число, обязательное поле).
    - rating: Рейтинг отзыва (тип: число от 1 до 5, обязательное поле).
    - comment: Комментарий к отзыву (тип: текстовая строка, необязательное поле).
    - created_at: Дата и время создания отзыва (тип: дата и время).
    - event_info: Информация о событии, связанном с отзывом (тип: объект, только для чтения).

    Примечания:
    - Поле "event_info" представляет собой сериализованное представление связанного события и доступно только для чтения.
    - Рейтинг должен быть числом от 1 до 5.
    """
    event_info = EventSerializer(source='event', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
