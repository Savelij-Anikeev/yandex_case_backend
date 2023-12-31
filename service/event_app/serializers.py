from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from rest_framework import serializers
from django.contrib.auth.models import Group
from .storage import Storage

from .models import Event, UserEventRelations, Category, EventCategoryRelations


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.StringRelatedField()
    organizer_id = serializers.IntegerField(read_only=True)
    photo = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('id', 'organizer', 'organizer_id', 'organizer_url', 'date_created', 
                            'date_updated', 'is_verified', 'free_places',)

    def get_image_url(self, obj):
        return obj.photo.url
        

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
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = EventCategoryRelations
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class AddEventNonAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'    
