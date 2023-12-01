from django.contrib import admin
from .models import Event, UserEventRelations

admin.site.register(Event)
admin.site.register(UserEventRelations)
