# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-16 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_location_map_placeholder'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]