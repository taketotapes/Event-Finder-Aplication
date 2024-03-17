from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """
        API endpoint для просмотра списка и создания новых уведомлений.

        list:
        Получить список всех уведомлений.

        create:
        Создать новое уведомление.
    """
    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'timestamp', 'read']
        read_only_fields = ['id', 'user', 'timestamp']
