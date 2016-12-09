from django.db import models

# Create your models here.
class Squawk(models.Model):
    text = models.CharField(max_length=140)
