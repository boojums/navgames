from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Event, Location, Series


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
    context_object_name = 'latest_events_list'

    def get_queryset(self):
        ''' Return the last five events '''
        return Event.objects.order_by('-start_date')[:5]


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

    # def get_queryset(self):
    #     self.event = get_object_or_404(Event, slug=self.kwargs['slug'])
    #     return self.event
