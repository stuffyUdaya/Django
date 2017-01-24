# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 19:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pairs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='person2friend', to='pair_app.Friends')),
                ('person1', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='person1friend', to='pair_app.Friends')),
            ],
        ),
    ]
