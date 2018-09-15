from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __repr__ (self):
        return "<Name: {} {}".format(self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=25)
    submitted_by = models.ForeignKey(User, related_name='submitted',blank=True,null=True)
    liked_by = models.ManyToManyField(User, related_name='liked_books')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __repr__ (self):
        return "<Title: {}".format(self.title)
