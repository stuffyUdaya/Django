from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import re
import bcrypt

# Create your models here.
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex  = re.compile(r'^[a-zA-Z]*$')

class UserManager(models.Manager):
    def userValidator(self,email,f_name,l_name,password,confpassword):
        errors = []
        flag= False
        if not email_regex.match(email):
            errors.append("Email was invalid")
            flag = True
        if len(email)<2:
            errors.append("Email must contain more than 2 characters")
            flag = True
        if len(f_name)<2:
            errors.append("First Name should contain atleast two characters")
            flag = True
        if not name_regex.match(f_name):
            errors.append("First Name was invalid")
            flag = True
        if len(l_name)<2:
            errors.append("Last Name should contain atleast two characters")
            flag = True
        if not name_regex.match(l_name):
            errors.append("Last Name was invalid")
            flag = True
        if password!=confpassword:
            errors.append("Passwords must match")
            flag = True
        if len(password)<5:
            errors.append("Password should contain atleast five characters")
            flag = True
        if not flag:
            pwhash = bcrypt.hashpw(str(password).encode(),bcrypt.gensalt())
            if User.objects.create(fname=f_name, lname=l_name, email=email, hashedpassword=pwhash):
                print "Reg Success"
                user = User.objects.last()
                return(flag,user)
            else:
                print "Reg Failed"
                return(flag,errors)
        return(flag, errors)
    def loginValidator(self, postData):
        try:

                 user= User.objects.get(email=postData['email'])
                 print "user", user
                 password = postData['password'].encode()
                 hashed = user.hashedpassword.encode()
                 if bcrypt.hashpw(password, hashed) == hashed :
                     return (True, user)
                 else:
                     return(False, "Login Credentials are invalid")

        except:
                     return(False, "Login Credentials are invalid " )
class User(models.Model):
    fname = models.CharField(max_length= 50)
    lname = models.CharField(max_length= 50)
    email = models.CharField(max_length= 150,unique= True)
    hashedpassword = models.CharField(max_length= 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
