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


class PastEvents(models.Manager):
    def get_queryset(self):
        return super(PastEvents, self).get_queryset() \
                .filter(start_date__lte=timezone.now())


class FutureEvents(models.Manager):
    def get_queryset(self):
        return super(FutureEvents, self).get_queryset() \
                .filter(start_date__gte=timezone.now())


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

    objects = models.Manager()
    past_events = PastEvents()
    future_events = FutureEvents()

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
    num_events = models.IntegerField(default=5)
    only_public = models.BooleanField(default=True)
    past_events = models.BooleanField(default=False)
    future_events = models.BooleanField(default=True)
    series = models.ForeignKey(Series, null=True, blank=True)

    def __str__(self):
        if self.past_events:
            descrip = 'Last '
        else:
            descrip = 'Next '
        if self.only_public:
            descrip += ' public '
        return descrip + str(self.num_events) + ' events.'


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