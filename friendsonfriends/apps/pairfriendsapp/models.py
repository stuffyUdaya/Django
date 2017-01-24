from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Friends(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)


class Friendships(models.Model):
    person2 = models.ForeignKey('Friends', models.DO_NOTHING, related_name="person3friend")

class Pairs(models.Model):
    # friendname = models.CharField(max_length=45, blank=True, null=True)
    # pairname =models.CharField(max_length=45, blank=True, null=True)
    friend = models.ForeignKey('Friends', models.DO_NOTHING, related_name="person2friend")
    person1 = models.ForeignKey('Friends', models.DO_NOTHING, related_name="person1friend")
