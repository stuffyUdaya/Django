from __future__ import unicode_literals

from django.db import models

from ..loginreg_app.models import User

class Courses(models.Model):
    name = models.CharField(max_length= 50)
    desc = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course_user = models.ForeignKey(User)
