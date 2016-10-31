from django.db import models
from datetime import datetime


# Create your models here.
class Squawker(models.Model):
    content = models.CharField(max_length=200)
    postdate = models.DateTimeField("postdate", default=datetime.now, blank=True)
