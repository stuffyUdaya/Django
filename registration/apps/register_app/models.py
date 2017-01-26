from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

# Create your models here.
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex  = re.compile(r'^[a-zA-Z]*$')

class UserManager(models.Manager):
    def userValidator(self,email,f_name,l_name,password,confpassword):
        errors = []
        if len(email) == 0:
            errors.append("Email is required")

        elif not email_regex.match(email):
            errors.append("Email was invalid and not added to database")
        elif len(email)<2:
            errors.append("Email must contain more than 2 characters")

        if len(f_name)<2:
            errors.append("First Name should contain atleast two characters")
        elif not name_regex.match(f_name):
            errors.append("First Name was invalid")

        if len(l_name)<2:
            errors.append("Last Name should contain atleast two characters")
        elif not name_regex.match(l_name):
            errors.append("Last Name was invalid")

        if password!=confpassword:
            errors.append("Passwords doesn't match")
        elif len(password)<5:
            errors.append("Password should contain atleast five characters")

        if len(errors) is not 0:
            return(False,errors)
        else:
            pwhash = bcrypt.hashpw(str(password),bcrypt.gensalt())
            information = User.objects.create(fname=f_name, lname=l_name, email=email, hashedpassword=pwhash)
            return(True,"passed")



        # # elif :
        # #     # Logins.objects.create(fname = f_name)
        # #     return(True,"First Name passed our Validations")
        # else:
        #     Logins.objects.create(fname = f_name)
        #     Logins.objects.create(email = email)
class User(models.Model):
    fname = models.CharField(max_length= 50)
    lname = models.CharField(max_length= 50)
    email = models.CharField(max_length= 150)
    hashedpassword = models.CharField(max_length= 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
