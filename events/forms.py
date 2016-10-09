from django.forms import ModelForm
from django.core.urlresolvers import reverse

from .models import Event, Location, Series


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_date', 'end_date',
                  'location', 'description', 'series']

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})
