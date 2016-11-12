from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
import datetime


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


class Club(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=10, unique=True)

    SCHOOL = 'S'
    CLUB = 'C'
    KIND_CHOICES = (
        (SCHOOL, 'School'),
        (CLUB, 'Club'),
    )
    kind = models.CharField(
        max_length=1,
        choices=KIND_CHOICES,
        default=SCHOOL)

    def __str__(self):
        return self.name


class Course(models.Model):
    event = models.ForeignKey(Event)
    name = models.CharField(max_length=20, null=True, blank=True)
    short_name = models.CharField(max_length=10)
    length = models.FloatField(null=True, blank=True)

    TIME = 'T'
    SCORE = 'S'
    BOTH = 'B'
    KIND_CHOICES = (
        (TIME, 'Time'),
        (SCORE, 'Score'),
        (BOTH, 'Both'),
    )
    kind = models.CharField(
        max_length=1,
        choices=KIND_CHOICES,
        default=TIME)

    def __str__(self):
        return '{}: {}'.format(self.event, self.name)


class Result(models.Model):
    course = models.ForeignKey(Course, null=True, blank=True)
    team_name = models.CharField(max_length=100)
    club = models.ForeignKey(Club, null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    time = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, default="OK")
    place = models.IntegerField()


    # TODO: template tag for this?
    def get_time(self):
        '''Returns the elapsed time as formatted string.'''
        hours = self.time // 3600
        seconds = self.time - hours
        minutes = seconds // 60
        seconds = seconds - (minutes * 60)
        if hours > 0:
            time = '{}:'.format(hours)
        else:
            time = ''
        time += "{:0>2}:{:0>2}".format(minutes, seconds)
        return time


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
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    club = models.ForeignKey(Club, null=True, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
