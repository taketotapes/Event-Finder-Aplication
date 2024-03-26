from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """
        API endpoint for viewing the list and creating new notifications.

        list:
        Get a list of all notifications.

        create:
        Create a new notification.
    """
    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'timestamp', 'read']
        read_only_fields = ['id', 'user', 'timestamp']
