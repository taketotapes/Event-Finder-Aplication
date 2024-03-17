from datetime import timedelta

from django.db.models import Q
from django.utils.timezone import datetime

from rest_framework import generics
from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated


class EventListView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """

        :return:
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
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class EventRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(organizer=self.request.user)


class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
