from django.shortcuts import get_object_or_404
from django.db.models import F

from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, IsAdminUser
from common_api_app.permissions import IsOwnerOrStaff

from .serializers import EventSerializer, UserEventRelationsSerializer, CategorySerializer
from .models import Event, UserEventRelations, Category


class EventAPIView(viewsets.ModelViewSet):
    """
        event crud
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = ()

    def get_permissions(self):
        """
            non organizer doesn1t have right to  use
            unsafe methods (Only GET)
        """
        if self.request.method not in SAFE_METHODS:
            self.permission_classes = (IsOwnerOrStaff,)
        
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.validated_data['organizer'] = self.request.user
        serializer.validated_data['free_places'] = serializer.validated_data['places']
        serializer.save()


class UserEventRelationsAPIView(viewsets.ModelViewSet):
    """
        crud event and user relations
    """
    queryset = UserEventRelations.objects.all()
    serializer_class = UserEventRelationsSerializer

    def get_queryset(self):
        """
            return only relations belongs to user; 
            if `is_staff` -> return all relations
        """
        if self.request.user.is_staff:
            return self.queryset
        return UserEventRelations.objects.filter(user=self.request.user.id)

    def get_object(self):
        """
            getting relation object by event`s id of current user;
        """
        obj = get_object_or_404(UserEventRelations, 
                                event=self.kwargs.get('pk'),
                                user=self.request.user.id)
        return obj

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.validated_data['user'] = self.request.user
            serializer.save()

            """counting free places"""
            event = get_object_or_404(Event, id=self.request.data['event'])
            event.free_places = event.places - len(UserEventRelations.objects.filter(event=event))
            event.save()

    
    def perform_destroy(self, instance):
        if self.request.user.is_authenticated:
            instance.delete()

            """counting free places"""
            event = get_object_or_404(Event, id=self.request.data['event'])
            event.free_places = event.free_places + 1
            event.save()

class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        """
            non organizer doesn1t have right to  use
            unsafe methods (Only GET)
        """
        if self.request.method not in SAFE_METHODS:
            self.permission_classes = (IsOwnerOrStaff,)
        
        return [permission() for permission in self.permission_classes]
    