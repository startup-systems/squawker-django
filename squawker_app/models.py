from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Squawk(models.Model):
    post = models.CharField(max_length=140)
    ts = models.DateTimeField()

    def __str__(self):
        return self.post