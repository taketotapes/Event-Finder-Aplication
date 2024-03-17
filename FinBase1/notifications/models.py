from django.db import models
from events.models import Event
from users.models import User


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    message = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.message}"
