from django.db import models
from datetime import datetime

class Squawk(models.Model):
    squawk_text = models.CharField(max_length = 140)
    timestamp = models.DateTimeField('date published')
    #def __str__(self):
    #   return self.squawk_text + "      " + self.timestamp
