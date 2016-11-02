from __future__ import unicode_literals

from django.db import models

class Squawk(models.Model):
    message = models.CharField(max_length=140)
    create_at = models.IntegerField(default=0)

    def __str__(self):
        return self.message
