from __future__ import unicode_literals
from django.db import models


class Squawker(models.Model):
    squawker_msg = models.CharField(max_length=140)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return squawker_msg
