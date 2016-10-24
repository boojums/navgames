# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20161007_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='series',
            field=models.ForeignKey(to='events.Series', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
