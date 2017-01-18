from itertools import chain
from operator import attrgetter

from django.utils.translation import ugettext_lazy as _
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from cms.utils.urlutils import admin_reverse
from rest_framework import viewsets, permissions

from .models import Event, Location
from .serializers import EventSerializer


class LocationList(generic.ListView):
    template_name = 'events/location_list.html'
    context_object_name = 'location_list'

    def get_queryset(self):
        return Location.objects.all()


class LocationDetail(generic.DetailView):
    model = Location
    fields = ['name', 'city', 'description']


class EventList(generic.ListView):
    template_name = 'events/event_list.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        ''' Return all upcoming events '''
        future_events = Event.future_events.all().order_by('start_date')
        if len(future_events) < 5:
            past_events = Event.past_events.all().order_by('-start_date')[:4]
            events = sorted(
                chain(future_events, past_events),
                key=attrgetter('start_date'))
        else:
            events = future_events
        return events


class EventCreate(CreateView):
    model = Event
    fields = ['name', 'start_date', 'end_date',
              'location', 'description', 'series', 'uses_epunch']
    success_url = reverse_lazy('index')


class EventUpdate(UpdateView):
    model = Event
    fields = ['name', 'start_date', 'end_date',
              'location', 'description', 'series']


class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('index')


class EventDetail(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'
    pk_url_kwarg = True

    def get_object(self):
        object = super(EventDetail, self).get_object()

        # Add an edit item to the CMS toolbar for this event
        menu = self.request.toolbar.get_or_create_menu('events-app', _('Events'))
        menu.add_sideframe_item(
            name=_('Edit this event'),
            url=admin_reverse('events_event_change', args=[object.pk]))

        return object

    # def get_queryset(self):
    #     self.event = get_object_or_404(Event, slug=self.kwargs['slug'])
    #     return self.event


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.future_events.all().order_by('start_date')
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
