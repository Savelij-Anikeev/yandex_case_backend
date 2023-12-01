from rest_framework import viewsets

from .serializers import EventSerializer
from .models import Event


class EventAPIView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


