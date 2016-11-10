from __future__ import unicode_literals

from django.db import models


class Squawks(models.Model):

    squawks_text = models.CharField(max_length=140)

    def __str__(self):
        return self.squawks_text
