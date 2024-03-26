from django.db import models
from events.models import Event
from users.models import User


class Notification(models.Model):
    """
    Model representing notifications for users regarding events.
    This model stores notifications for users regarding specific events.
    Each notification contains a message, an associated event, and a timestamp.
    It also tracks whether the notification has been read by the user.
    Attributes:
        user (ForeignKey): The user to whom the notification is directed.
        event (ForeignKey): The event associated with the notification.
        message (TextField): The message content of the notification.
        read (BooleanField): Indicates whether the notification has been read by the user.
        timestamp (DateTimeField): The timestamp representing when the notification was created.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    message = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the notification.
        :return: String representation of the notification.
        """
        return f"{self.user.username}: {self.message}"
