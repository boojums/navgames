from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser

from .models import Event, Race
from .serializers import EventSerializer, RaceSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-start_date')
    serializer_class = EventSerializer


class RaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows races to be viewed or edited.
    """
    parser_classes = (FileUploadParser,)
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
