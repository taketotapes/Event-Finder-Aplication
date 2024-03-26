from rest_framework import serializers
from .models import Ticket, User


class UserSerializer(serializers.ModelSerializer):
    """
        Serializer for the user.

        Fields:
        - id: Unique user identifier (type: integer).
        - first_name: User's name (type: string).
        - last_name: User's last name (type: string).
    """
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class TicketSerializer(serializers.ModelSerializer):
    """
        Serializer for a ticket.

        Fields:
        - event: The event for which the ticket was purchased (type: integer, required field).
        - owner: Ticket owner (type: user object, filled in automatically).
        - price: Ticket price (type: decimal).
        - num_tickets: Number of tickets (type: integer).
        - purchase_date: Ticket purchase date (type: date).
        - timestamp: Time stamp of ticket creation (type: date and time, read only).

        Notes:
        - The "owner" field is automatically filled in by the current user who completed the ticket creation request.
    """
    class Meta:
        model = Ticket
        fields = ['event', 'owner', 'price', 'num_tickets', 'purchase_date', 'timestamp']

    def create(self, validated_data):
        """
            Method for creating a new ticket.

            Options:
            - validated_data: Dictionary with data for creating a ticket.

            Returns:
            - Created ticket object.
        """
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
