# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-16 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_eventlistpluginmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='series',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]