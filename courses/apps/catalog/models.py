from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        if len(postData['name']) == 0:
            errors.append('Course must have title!')
        if len(postData['descrip']) < 15:
            errors.append('Course description must have 15 characters minimum!')
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    descrip = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()

