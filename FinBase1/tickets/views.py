from .models import Ticket
from rest_framework import generics
from .serializers import TicketSerializer
from rest_framework.permissions import IsAuthenticated


class TicketListView(generics.ListAPIView):
    """
    API endpoint to list all tickets.

    Attributes:
        serializer_class (Serializer): Serializer class used for serializing/deserializing tickets.
        permission_classes (list): List of permission classes that the view requires for accessing.
    """
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Get queryset of all tickets.

        :return: All tickets queryset.
        """
        queryset = Ticket.objects.all()
        return queryset


class TicketCreateView(generics.CreateAPIView):
    """
    API endpoint to create a new ticket.

    Attributes:
        serializer_class (Serializer): Serializer class used for serializing/deserializing tickets.
        permission_classes (list): List of permission classes that the view requires for accessing.
    """
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Perform creation of a new ticket.

        :param serializer: Serializer instance.
        """
        serializer.save(owner=self.request.user)


class TicketDetailView(generics.RetrieveDestroyAPIView):
    """
    API endpoint to retrieve and delete an individual ticket.

    Attributes:
        queryset (QuerySet): Queryset representing all tickets.
        serializer_class (Serializer): Serializer class used for serializing/deserializing tickets.
        permission_classes (list): List of permission classes that the view requires for accessing.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
