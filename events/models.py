from django.db import models
from django.template.defaultfilters import slugify


class Location(models.Model):
    ''' A location for an event.'''
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    maplink = models.URLField(blank=True)

    def __str__(self):
        return self.name + ', ' + self.city


class Series(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Series'

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
    slug = models.SlugField(unique=True)

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
