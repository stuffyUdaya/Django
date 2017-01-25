from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class emailManager(models.Manager):
    def emailValidator(self,email):
        if email_regex.match(email):
            Email.objects.create(emailAddress = email)
            return (True, "Email was valid and added to database.")
        if not email_regex.match(email):
            return(False,"Email was invalid and not added to database")


class Email(models.Model):
    emailAddress = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = emailManager()




class UserManager(models.Manager):
      def login(self, email, password):
          print "Running a login function!"
          print ("If successful login occurs, maybe return {'theuser':user} where user is a user object?")
          print ("If unsuccessful, maybe return { 'errors':['Login unsuccessful'] }")
          return("I will be a future login method for coding dojo students")
      def register(self, **kwargs):
          print ("Register a user here")
          print ("If successful, maybe return {'theuser':user} where user is a user object?")
          print ("If unsuccessful do something like this? return {'errors':['User first name to short', 'Last name too short'] ")
          pass
class User(models.Model):
      first_name = models.CharField(max_length=45)
      last_name = models.CharField(max_length=45)
      password = models.CharField(max_length=100)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      # *************************
      # Connect an instance of UserManager to our User model overwriting
      # the old hidden objects key with a new one with extra properties!!!
      userManager = UserManager()

      # *************************
