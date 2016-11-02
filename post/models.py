from django.db import models

# Create your models here.
class posts(models.Model):
    message = models.CharField(max_length=140)
    post_time = models.FloatField()