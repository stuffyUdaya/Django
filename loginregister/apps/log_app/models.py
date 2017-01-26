from __future__ import unicode_literals

from django.db import models

from django.contrib import messages

import re

# Create your models here.
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex  = re.compile(re.compile(r'^[a-zA-Z]*$')
class emailManager(models.Manager):
    def emailValidator(self,email,f_name,l_name,password,confpassword):
        if email_regex.match(email):
            # Logins.objects.create(email = email)
            return (True, "Email was valid and added to database.")
        elif not email_regex.match(email):
            return(False,"Email was invalid and not added to database")
        elif len(email)<2:
            return()

        elif len(f_name)<2:
            return(False,"First Name should contain atleast two characters")
        elif not str.isalpha(str(f_name)):
            return(False,"FIrst Name must contain letters")
        # elif :
        #     # Logins.objects.create(fname = f_name)
        #     return(True,"First Name passed our Validations")
        else:
            Logins.objects.create(fname = f_name)
            Logins.objects.create(email = email)

class fnameManager(models.Manager):
    def fnameValidator(self,f_name):
        if len(f_name)<2:
            return(False,"First Name should contain atleast two characters")
        elif not str.isalpha(str(f_name)):
            return(False,"FIrst Name must contain letters")
        else:
            Logins.objects.create(fname = f_name)
            return(True,"First Name passed our Validations")




class Logins(models.Model):
    fname = models.CharField(max_length= 50, blank =True, null= True)
    lname = models.CharField(max_length= 50, blank =True, null= True)
    email = models.CharField(max_length= 150, blank =True, null= True)
    hashedpassword = models.CharField(max_length= 255, blank =True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = emailManager()
    objects1 = fnameManager()
