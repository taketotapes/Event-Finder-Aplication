from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from events.models import Event, Attendance
from users.models import User
from django.db.models import Count, Sum


class Ticket(models.Model):
    """
    Model representing a ticket for an event.

    Attributes:
        event (ForeignKey): The event for which the ticket is purchased.
            Related name: 'event'
            On deletion of the event, the ticket is also deleted (CASCADE).
        owner (ForeignKey): The user who purchased the ticket.
            Related name: 'owner'
            On deletion of the user, the ticket is also deleted (CASCADE).
        price (DecimalField): The price of the ticket.
        purchase_date (DateTimeField): The date and time when the ticket was purchased. Automatically set to the current
        date and time when the ticket is created.
        num_tickets (PositiveIntegerField): The number of tickets purchased.
        timestamp (DateTimeField): The date and time when the ticket was last updated or created. Automatically set to
        the current date and time when the ticket is updated or created.

        Methods:
            __str__: Returns a string representation of the ticket, including the event title.
            save: Custom save method to ensure that the ticket price cannot be changed by anyone other than the event
                organizer, and to check if there are enough available tickets for purchase before saving.
        """
    STATUS_CHOICES = [
        ('active', 'Активний'),
        ('finished', 'Фінішед'),
        ('cancelled', 'Скасований'),
    ]

    event = models.ForeignKey(Event, related_name='event', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)
    num_tickets = models.PositiveIntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"Ticket for {self.event.title}"

    def save(self, *args, **kwargs):
        """
        Custom save method to ensure that the ticket price cannot be changed by anyone other than the event organizer,
        and to check if there are enough available tickets for purchase before saving.
        """
        if self.pk:
            if self.owner != self.event.organizer:
                raise ValueError('Only the organizer can change the ticket price.')
        attendees_count = self.event.attendees.aggregate(Sum('num_tickets'))['num_tickets__sum']
        if attendees_count is None:
            attendees_count = 0
        if self.num_tickets > self.event.capacity - attendees_count:
            raise ValueError("There are not enough available tickets for this event.")
        super().save(*args, **kwargs)

    