from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512, blank=True, null=True)
    place = models.CharField(max_length=128)
    date_start = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    organizer = models.ForeignKey(User, on_delete=models.PROTECT)
    is_verified = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    places = models.PositiveIntegerField(default=0)
    free_places = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'id: {self.id} event: {self.name}'
