from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Review
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
