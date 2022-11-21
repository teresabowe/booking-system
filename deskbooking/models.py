from django.db import models
from django.contrib.auth.models import User


class Desk(models.Model):
    desk = models.CharField(max_length=20, unique=True)
    floor = models.CharField(max_length=200, unique=False)
    description = models.CharField(max_length=200, unique=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["desk"]

    def __str__(self):
        return f'{self.desk}'


class Booking(models.Model):
    desk_booking_date = models.DateField(null=True, blank=True)
    desk = models.ForeignKey(Desk, on_delete=models.CASCADE,
                             related_name="desk_booking")
    desk_user = models.ForeignKey(User, null=True, blank=True,
                                  on_delete=models.CASCADE,
                                  related_name="user_booking")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
        unique_together = (('desk_booking_date', 'desk',),
                           ('desk_booking_date', 'desk_user',))

    def __str__(self):
        return f'{self.desk}'
