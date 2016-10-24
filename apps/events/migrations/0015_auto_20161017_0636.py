# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-17 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20161016_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventlistpluginmodel',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eventlistpluginmodel',
            name='only_public',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='eventlistpluginmodel',
            name='series',
            field=models.ManyToManyField(blank=True, to='events.Series'),
        ),
        migrations.AddField(
            model_name='eventlistpluginmodel',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='eventlistpluginmodel',
            name='n_events',
            field=models.IntegerField(default=5),
        ),
    ]