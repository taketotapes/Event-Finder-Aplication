from django.utils import timezone

from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Review
from tickets.models import Ticket
from events.models import Event
from .serializers import ReviewSerializer


class ReviewListCreate(generics.ListCreateAPIView):
    """
    API endpoint to list and create reviews.

    Attributes:
        queryset (QuerySet): Queryset representing all reviews.
        serializer_class (Serializer): Serializer class used for serializing/deserializing reviews.
        permission_classes (list): List of permission classes that the view requires for accessing.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        event_id = request.data.get('event_id')
        user = request.user
        event = get_object_or_404(Event, id=event_id)

        if event.datetime > timezone.now():
            return Response({"error": "Это событие еще не прошло"}, status=status.HTTP_400_BAD_REQUEST)

        if not Ticket.objects.filter(user=user, event=event).exists():
            return Response({"error": "У вас нет билета на это событие"}, status=status.HTTP_400_BAD_REQUEST)

        return super().post(request, *args, **kwargs)


class ReviewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, and delete individual reviews.

    Attributes:
        queryset (QuerySet): Queryset representing all reviews.
        serializer_class (Serializer): Serializer class used for serializing/deserializing reviews.
        permission_classes (list): List of permission classes that the view requires for accessing.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
