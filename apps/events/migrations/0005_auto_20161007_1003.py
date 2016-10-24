# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20161007_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='title',
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='series',
            field=models.ForeignKey(to='events.Series', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='maplink',
            field=models.URLField(blank=True),
        ),
    ]
