from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django.core.auth.models import User
from django import forms
from .models import Event, Location, Series, UserProfile


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_date', 'end_date',
                  'location', 'description', 'series']

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('club', 'school')
