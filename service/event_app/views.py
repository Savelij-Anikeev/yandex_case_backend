from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS
from common_api_app.permissions import IsOwnerOrStaff

from .serializers import EventSerializer, UserEventRelationsSerializer
from .models import Event, UserEventRelations


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
    