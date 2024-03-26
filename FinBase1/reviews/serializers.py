from rest_framework import serializers
from events.serializers import EventSerializer
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for reviews.

    Fields:
    - id: Unique review identifier (type: integer).
    - event: Event associated with the review (type: integer, required field).
    - rating: Review rating (type: number from 1 to 5, required field).
    - comment: Comment for the review (type: text string, optional field).
    - created_at: Date and time the review was created (type: date and time).
    - event_info: Information about the event associated with the review (type: object, read-only).

    Notes:
    - The "event_info" field is a serialized representation of the associated event and is read-only.
    - The rating must be a number from 1 to 5.
    """
    event_info = EventSerializer(source='event', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
