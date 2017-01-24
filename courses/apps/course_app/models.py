from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length= 50, blank =True, null=True)
    desc = models.TextField(max_length=200, blank = True, null =True)
    created_at=models.DateTimeField(blank=True,null=True)
    
