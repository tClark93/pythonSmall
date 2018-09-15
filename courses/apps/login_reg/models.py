from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')

class UserManager(models.Manager):
    def valid(self, postData):
        errors = []
        if not postData['first_name'].isalpha():
            errors.append('Name can only contain alphabetical characters!')
        if len(postData['first_name']) < 2:
            errors.append('First name must be at least two letters!')
        if not postData['last_name'].isalpha():
            errors.append('Name can only contain alphabetical characters!')
        if len(postData['last_name']) < 2:
            errors.append('Last name must be at least two letters!')
        if not re.match(EMAIL_REGEX, postData['email']):
            errors.append('Email is not valid.')
        if len(postData['password']) < 6:
            errors.append('Password must contain at least 6 characters!')
        if postData['password'] != postData['confirm']:
            errors.append('Passwords must match!')
        if User.objects.filter(email = postData['email']):
            errors.append('Email already exists.')
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()