from django.db import models
from django.contrib.auth.models import User
import PIL

class Event(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512, blank=True, null=True)
    place = models.CharField(max_length=128)
    date_start = models.CharField(max_length=128)
    time_start = models.CharField(max_length=5)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    organizer = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ManyToManyField('Category', through='EventCategoryRelations')

    is_verified = models.BooleanField(default=False)

    cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    places = models.PositiveIntegerField(default=0)
    free_places = models.PositiveIntegerField(default=0)

    photo = models.CharField(max_length=1024, default=None, null=True)

    def __str__(self) -> str:
        return f'id: {self.id} event: {self.name}'


class Category(models.Model):
    name = models.CharField(max_length=32)


class UserEventRelations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_event_rel_user')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.id}'


class EventCategoryRelations(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

