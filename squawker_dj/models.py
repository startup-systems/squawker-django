from django.db import models
import datetime


# Create your models here.
class Squawk(models.Model):
    text = models.CharField(max_length=140)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
