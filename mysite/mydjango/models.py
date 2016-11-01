# from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Squawker(models.Model):
    post = models.CharField(max_length=140)
    # time = models.DateTimeField(datetime.now())