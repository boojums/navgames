# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20161007_1003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name_plural': 'Series'},
        ),
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(unique=True, default=''),
            preserve_default=False,
        ),
    ]
