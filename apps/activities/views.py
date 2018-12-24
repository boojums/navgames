from itertools import chain
from operator import attrgetter

from django.utils.translation import ugettext_lazy as _
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from cms.utils.urlutils import admin_reverse
from rest_framework import viewsets, permissions

from .models import Activity, Lesson


class ActivityList(generic.ListView):
    template_name = 'activities/activity_list.html'
    context_object_name = 'activity_list'

    def get_queryset(self):
        ''' Return all activities '''
        return Activity.objects.all()

class ActivityCreate(CreateView):
    model = Activity
    fields = ['name', 'description']
    success_url = reverse_lazy('index')


class ActivityUpdate(UpdateView):
    model = Activity
    fields = ['name', 'description']


class ActivityDelete(DeleteView):
    model = Activity
    success_url = reverse_lazy('index')


class ActivityDetail(generic.DetailView):
    model = Activity
    template_name = 'activities/detail.html'
    pk_url_kwarg = True

    def get_object(self):
        object = super(ActivityDetail, self).get_object()

        # Add an edit item to the CMS toolbar for this event
        menu = self.request.toolbar.get_or_create_menu(
            'activities-app', _('Activities'))
        menu.add_sideframe_item(
            name=_('Edit this activity'),
            url=admin_reverse('activities_activity_change', args=[object.pk]))

        return object



