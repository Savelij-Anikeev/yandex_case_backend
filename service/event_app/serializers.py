from rest_framework import serializers

from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('id', 'organizer', 'date_created', 
                            'date_updated', 'is_verified', 'free_places')
