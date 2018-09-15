from __future__ import unicode_literals
from django.db import models

class Post(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)