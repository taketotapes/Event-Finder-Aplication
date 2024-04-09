from datetime import timedelta, timezone

from django.db.models import Q
import datetime

from rest_framework import generics, status
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated


class EventListView(generics.ListAPIView):
    """
    A view for listing events based on various filters.

    This view retrieves a queryset of events based on specified filters such as location, category, date, and search query.
    It requires authentication for access.

    Supported query parameters:
        - location: Filter events by location (case insensitive).
        - category: Filter events by category (case insensitive).
        - date: Filter events by date. Format: 'YYYY-MM-DD'.
        - search: Search events by title or description containing the provided query string (case insensitive).
    """
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
            Get the queryset of events based on request parameters.

            :return: A filtered queryset of events.
        """
        queryset = Event.objects.all()
        location = self.request.query_params.get('location', None)
        category = self.request.query_params.get('category', None)
        date = self.request.query_params.get('date', None)
        search_query = self.request.query_params.get('search', None)

        if location:
            queryset = queryset.filter(location__icontains=location)
        if category:
            queryset = queryset.filter(category__icontains=category)
        if date:
            try:
                date_obj = datetime.strptime(date, '%Y-%m-%d')
                queryset = queryset.filter(date__gte=date_obj, date__lt=date_obj + timedelta(days=1))
            except ValueError:
                raise 'Invalid date format'
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

        return queryset


class EventCreateView(generics.CreateAPIView):
    """
    A view for creating new events.

    This view allows authenticated users to create new events by providing event data.
    It utilizes the EventSerializer for serialization and deserialization of event data.
    Requires authentication for access.

    When a new event is created, the current user is automatically assigned as the organizer.
    """

    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Perform the creation of a new event.

        :param serializer: EventSerializer instance for serializing event data.
        """
        serializer.save(organizer=self.request.user)


class EventRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    A view for retrieving, updating, and deleting events.

    This view allows authenticated users to retrieve, update, and delete existing events by their primary key.
    Utilizes the EventSerializer for serialization and deserialization of event data.
    Requires authentication for access.

    When updating an event, the current user must be the organizer of the event.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        """
        Perform the update of an existing event.

        :param serializer: EventSerializer instance for serializing event data.
        """
        serializer.save(organizer=self.request.user)


class EventDetailView(generics.RetrieveAPIView):
    """
    A view for retrieving details of a specific event.

    This view allows authenticated users to retrieve details of a specific event by its primary key.
    Utilizes the EventSerializer for serialization of event data.
    Requires authentication for access.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
