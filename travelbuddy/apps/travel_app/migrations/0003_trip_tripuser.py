# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0002_trip_tripmanager'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='tripuser',
            field=models.ManyToManyField(to='travel_app.User'),
        ),
    ]