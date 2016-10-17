from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField


# TODO: flesh out. Street address and/or coordinates?
class Location(models.Model):
    ''' A location for an event.'''
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    maplink = models.URLField(blank=True)
    description = models.TextField(blank=True)
    map_placeholder = PlaceholderField('map')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Location, self).save(*args, **kwargs)

    def __str__(self):
        return self.name + ', ' + self.city


# TODO: active? Date range? more info?
class Series(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Series'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Series, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Event(models.Model):
    ''' Event information, including times and description.'''
    name = models.CharField(max_length=100, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    location = models.ForeignKey(Location)
    description = models.TextField()
    uses_epunch = models.BooleanField()
    series = models.ForeignKey(Series, null=True, blank=True)
    public = models.BooleanField()
    slug = models.SlugField(unique=True)

    @property
    def future(self):
        now = timezone.now()
        return self.start_date > now

    @property
    def past(self):
        now = timezone.now()
        return self.start_date < now

    def save(self, *args, **kwargs):
        if not self.name:
            slugname = self.location.name + ' ' + str(self.start_date.year)
            self.slug = slugify(slugname)
        else:
            self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        if not self.name:
            descrip = self.location.name + ' (' + str(self.start_date) + ')'
        else:
            descrip = self.name + ', ' + ' (' + str(self.start_date) + ')'
        return descrip


class EventPluginModel(CMSPlugin):
    event = models.ForeignKey(Event)

    def __str__(self):
        return self.event.name


class EventListPluginModel(CMSPlugin):
    n_events = models.IntegerField(default=5)
    only_public = models.BooleanField(default=True)
    only_future = models.BooleanField(default=True)
    only_past = models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True,
                                  help_text='Only use this instead of future '
                                  'or past if you want a static date range')
    end_date = models.DateField(null=True, blank=True)
    series = models.ManyToManyField(Series, blank=True)

    def __str__(self):
        return 'Next ' + str(self.n_events) + ' events.'


# TODO: I don't think these belongs here --
# not sure, part of a registration app?
class Club(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=10, unique=True)


class School(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=10, unique=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    club = models.ForeignKey(Club, null=True, blank=True)
    school = models.ForeignKey(School, null=True, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
