from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
       Serializer for the user.

       Fields:
       - id: Unique user identifier (type: integer).
       - username: Username (type: string).
       - first_name: User's name (type: string).
       - last_name: User's last name (type: string).
       - country: User's country (type: string).
       - city: User's city (type: string).
       - street: User street (type: string).
       - phone: User's phone number (type: integer).
       - telegram_url: URL of the user's Telegram profile (type: string).
       - password: User password (type: string, write-only).

       Notes:
       - The "password" field is write-only (write_only=True), and is not included in the output by default.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'country', 'city', 'street', 'phone', 'telegram_url']
        extra_kwargs = {'password': {'write_only': True}}


class UserPassChangeSerializer(serializers.Serializer):
    """
        Serializer for changing user password.

        Fields:
        - old_pass: Old user password (type: string, required field).
        - new_pass: New user password (type: string, required field).

        Notes:
        - Both fields are required.
    """
    old_pass = serializers.CharField(required=True)
    new_pass = serializers.CharField(required=True)
