from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone
# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Board(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField(max_length=200)

    def __str__(self):
        return self.title