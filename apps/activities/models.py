from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager


class Activity(models.Model):
    ''' A single activity that could be part of a lesson. '''
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    tags = TaggableManager()
    objectives = models.TextField()
    standards = models.TextField(blank=True)
    time_required = models.DurationField()
    materials = models.TextField(blank=True)
    
    prep = models.TextField(blank=True)
    intro = models.TextField(blank=True)
    execution = models.TextField(blank=True)
    variations = models.TextField(blank=True)
    reflection = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Activity, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    tags = TaggableManager()

    def __str__(self):
        return self.name
