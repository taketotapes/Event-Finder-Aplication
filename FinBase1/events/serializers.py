from rest_framework import serializers

from .models import Event
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
        Serializer for user.

        Fields:
        - id: Unique user identifier (type: integer).
        - first_name: Username (type: string).
        - last_name: User Last name (type: string).

        Notes:
        - The "id" field is automatically generated and is read-only.
    """
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class EventSerializer(serializers.ModelSerializer):
    """
       Serializer for the event.

       Fields:
       - attendees_count: Number of event participants (type: integer, read-only).
       - organizer: Event organizer (type: user object, serialized using UserSerializer).
       - title: Event title (type: string).
       - description: Description of the event (type: string).
       - date: Event date (type: date).
       - location: Location of the event (type: string).
       - category: Event category (type: string).
       - capacity: Event capacity (type: integer).
       - bookings: Number of bookings for the event (type: integer).

       Notes:
       - The "attendees_count" field is calculated using the get_attendees_count method and is read-only.
    """
    organizer = UserSerializer
    attendees_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['attendees_count', 'organizer', 'title', 'description', 'date', 'location', 'category',
                  'capacity', 'bookings']

    def get_attendees_count(self, obj):
        """
            Method for getting the number of participants in an event.

            Returns the number of records in the associated attendee field of the Event model.

            Options:
            - obj: An instance of the event object.

            Returns:
            - Number of event participants (type: integer).
        """
        return obj.attendees.count()
