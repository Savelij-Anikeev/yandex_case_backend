from django.shortcuts import get_object_or_404
from django.db.models import F
from django.contrib.auth.models import Group

from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import SAFE_METHODS, IsAdminUser
from common_api_app.permissions import IsOwnerOrStaff, IsInstitutionWorkerOrStaff

from .serializers import (EventSerializer, UserEventRelationsSerializer, 
                        CategorySerializer, EventCategoryRelationsSerializer, 
                        UserSerializer, GroupSerialzier, AddEventNonAuthSerializer)
from .models import Event, UserEventRelations, Category, EventCategoryRelations

from .storage import Storage



class EventAPIView(viewsets.ModelViewSet):
    """
        event crud
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = ()

    def get_queryset(self):
        """
            custom queryset
            get params: verified=(bool)
        """
        if 'verified' in self.request.GET.keys():
            """is verified"""
            if self.request.GET.get('verified') == 'false':
                qs =  Event.objects.filter(is_verified=False)   
            if self.request.GET.get('verified') == 'all':
                qs =  Event.objects.all() 
            else:
                qs = Event.objects.all()
        else:
            qs = Event.objects.filter(is_verified=True)
        return qs

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
    """
        crud for category: each person can read,
        but only admin can change/delete
    """
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
    

class EventCategoryRelationsAPIView(viewsets.ModelViewSet):

    """
        manages event and category relation
    """
    queryset = EventCategoryRelations.objects.all()
    serializer_class = EventCategoryRelationsSerializer

    def get_object(self):
        """you should make get request with `category` param"""
        obj = get_object_or_404(EventCategoryRelations, 
                                event=self.kwargs.get('pk'),
                                category=self.request.data.get('category')
                                )
        return obj

    def perform_create(self, serializer):
        serializer.save()

    def get_permissions(self):
        """
            non organizer doesn1t have right to  use
            unsafe methods (Only GET)
        """
        if self.request.method not in SAFE_METHODS:
            self.permission_classes = (IsOwnerOrStaff,)
            
        return [permission() for permission in self.permission_classes]
    

class SetUserGroup(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsInstitutionWorkerOrStaff,)
    

class GroupListAPIView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerialzier


class VerifyEventAPIView(generics.RetrieveUpdateAPIView):
    """verify events"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsInstitutionWorkerOrStaff,)

    def perform_update(self, serializer):
        """change field"""
        serializer.validated_data['is_verified'] = self.request.data.get('is_verified')
        serializer.save()


class AddEventNonAuthAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = AddEventNonAuthSerializer

    def perform_create(self, serializer):
        serializer.validated_data['organizer'] = None
        serializer.save()



# checking when user models gets new instance and giving it student group
# @receiver(models.signals.post_save, sender=User)
# def post_save_user_signal_handler(sender, instance, created, **kwargs):
#     if created:
#        group = Group.objects.get(name='students')
#        instance.groups.add(group)
#        instance.save()






