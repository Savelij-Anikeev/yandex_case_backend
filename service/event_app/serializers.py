from django.urls import reverse
from django.contrib.sites.models import Site
from rest_framework import serializers

from .models import Event, UserEventRelations, Category, EventCategoryRelations


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.StringRelatedField()
    organizer_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('id', 'organizer', 'organizer_id', 'organizer_url', 'date_created', 
                            'date_updated', 'is_verified', 'free_places',)
        

class UserEventRelationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserEventRelations
        fields = ('id', 'user', 'event',)
        read_only_fields = ('id', 'user',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EventCategoryRelationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategoryRelations
        fields = '__all__'
