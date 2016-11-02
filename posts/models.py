from django.db import models

# Create your models here.
class Squawkers(models.Model):
    squawkers_text = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date published')

