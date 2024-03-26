from django.db import models
from users.models import User
from events.models import Event


class Review(models.Model):
    """
    Model representing a review for an event.

    Attributes:
        event (ForeignKey): The event being reviewed. On deletion of the event, the review is also deleted (CASCADE).
        user (ForeignKey): The user who created the review. On deletion of the user, the review is also deleted
        (CASCADE).
        rating (IntegerField): The rating given to the event, ranging from 1 to 5.
        comment (TextField): The comment or feedback for the event.
        created_at (DateTimeField): The date and time when the review was created. Automatically set to the current
        date and time when the review is created.
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
