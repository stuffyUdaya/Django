# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pairfriendsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pairs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendname', models.CharField(blank=True, max_length=45, null=True)),
                ('pairname', models.CharField(blank=True, max_length=45, null=True)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='person2friend', to='pairfriendsapp.Friends')),
            ],
        ),
    ]