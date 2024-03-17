from django.db import models
from users.models import User


class Event(models.Model):
    organizer = models.ForeignKey(User, related_name='events_organized', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField(default=100)
    bookings = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ['organizer', 'title']

    def __str__(self):
        return f'{self.organizer} {self.title}'


class Attendance(models.Model):
    event = models.ForeignKey(Event, related_name='attendees', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='attended_events', on_delete=models.CASCADE)
    num_tickets = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['event', 'user']
