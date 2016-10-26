# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-26 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('liveresults', '0002_auto_20161026_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='races', to='liveresults.Event'),
        ),
    ]