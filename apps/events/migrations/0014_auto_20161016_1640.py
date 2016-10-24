# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-16 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_location_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='slug',
            field=models.SlugField(default='default', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]