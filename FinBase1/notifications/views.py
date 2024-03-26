from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer


class NotificationListCreate(generics.ListCreateAPIView):
    """
    API endpoint to list and create notifications.

    - `GET` returns a list of all notifications for the user.
    - `POST` allows creating new notifications.
    - Requires user authentication.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Perform creation of notification.

        :param serializer: Serializer instance.
        """
        serializer.save(user=self.request.user)


class NotificationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, and delete individual notifications.

    - `GET` returns information about a notification.
    - `PUT` and `DELETE` allow updating and deleting notifications respectively.
    - Requires user authentication.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]


class UnreadNotificationList(generics.ListAPIView):
    """
    API endpoint to list unread notifications for the user.

    - Returns only unread notifications.
    - Requires user authentication.
    """
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Get queryset of unread notifications.

        :return: Unread notifications queryset.
        """
        return Notification.objects.filter(user=self.request.user, is_read=False)


class MarkAsRead(generics.UpdateAPIView):
    """
    API endpoint to mark a notification as read.

    - Accepts a request to mark a specific notification as read.
    - Requires user authentication.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Get the notification object to mark as read.

        :return: Notification object.
        """
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs['pk'])
        obj.is_read = True
        obj.save()
        return obj


class ClearAllNotifications(generics.DestroyAPIView):
    """
    API endpoint to clear all notifications for the user.

    - Accepts a request to delete all notifications for the user.
    - Requires user authentication.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        """
        Delete all notifications for the user.

        :param request: Request object.
        :param args: Additional arguments.
        :param kwargs: Additional keyword arguments.
        :return: Response.
        """
        user_notifications = self.get_queryset().filter(user=request.user)
        user_notifications.delete()
        return self.destroy(request, *args, **kwargs)