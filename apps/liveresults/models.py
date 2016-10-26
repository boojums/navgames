from django.db import models
from django.utils import timezone


class PastEvents(models.Manager):
    def get_queryset(self):
        return super(PastEvents, self).get_queryset() \
                .filter(start_date__lte=timezone.now())


class FutureEvents(models.Manager):
    def get_queryset(self):
        return super(FutureEvents, self).get_queryset() \
                .filter(start_date__gte=timezone.now())


class Event(models.Model):
    ''' Event metadata '''
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

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

    def __str__(self):
        return self.name


class Race(models.Model):
    ''' An individual race as part of a single or multi-day event. '''
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100, null=True, blank=True)

    # TODO: smart filenames
    startlist = models.FileField(upload_to='liveresults/')
    resultslist = models.FileField(upload_to='liveresults/')
    event = models.ForeignKey(Event, related_name='races')

    def __str__(self):
        return self.name
