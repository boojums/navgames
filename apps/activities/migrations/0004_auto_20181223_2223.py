# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-12-24 03:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_auto_20181223_2202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='descriptions',
            new_name='description',
        ),
    ]
