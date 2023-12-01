from rest_framework import serializers

from .models import Event, UserEventRelations

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('id', 'organizer', 'date_created', 
                            'date_updated', 'is_verified', 'free_places',)


class UserEventRelationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEventRelations
        fields = ('id', 'user', 'event',)
        read_only_fields = ('id', 'user',)
