from __future__ import unicode_literals

from django.db import models

class Squawks(models.Model):
    msg = models.CharField(max_length=140)
    timestamp = models.DateTimeField('Date Published', auto_now_add=True)

    def __str__(self):
        return self.msg + " at " + str(timestamp)

    class Meta:
        ordering = ['-timestamp']
