from django.contrib import admin
from .models import Event, UserEventRelations, Category, EventCategoryRelations

admin.site.register(Event)
admin.site.register(UserEventRelations)
admin.site.register(Category)
admin.site.register(EventCategoryRelations)
