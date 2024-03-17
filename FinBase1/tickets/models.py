from django.db import models
from events.models import Event, Attendance
from users.models import User
from django.db.models import Count, Sum


class Ticket(models.Model):
    event = models.ForeignKey(Event, related_name='event', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)
    num_tickets = models.PositiveIntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket for {self.event.title}"

    def save(self, *args, **kwargs):
        if self.pk:
            if self.owner != self.event.organizer:
                raise ValueError('Only the organizer can change the ticket price.')
        attendees_count = self.event.attendees.aggregate(Sum('num_tickets'))['num_tickets__sum']
        if attendees_count is None:
            attendees_count = 0
        if self.num_tickets > self.event.capacity - attendees_count:
            raise ValueError("There are not enough available tickets for this event.")
        super().save(*args, **kwargs)
