from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Squawker(models.Model):
    message = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.message
# Create your models here.
