from datetime import timezone

from django.db import models
from users.models import User


class Event(models.Model):
    """
    Model representing an event.
    Attributes:
        organizer (ForeignKey): Reference to the User who organized the event.
        title (CharField): Title of the event.
        description (TextField): Description of the event.
        date (DateField): Date of the event.
        location (CharField): Location of the event.
        category (CharField): Category of the event.
        capacity (PositiveIntegerField): Maximum capacity of attendees for the event.
        bookings (PositiveIntegerField): Number of bookings made for the event.
    """

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
    """
    Model representing attendance of users at events.
    Attributes:
        event (ForeignKey): Reference to the Event being attended.
        user (ForeignKey): Reference to the User attending the event.
        num_tickets (PositiveIntegerField): Number of tickets reserved by the user for the event.
    """

    event = models.ForeignKey(Event, related_name='attendees', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='attended_events', on_delete=models.CASCADE)
    num_tickets = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['event', 'user']