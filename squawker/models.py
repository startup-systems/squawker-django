from django.apps import AppConfig
from django.db import models


class Squawks(models.Model):

    squawk = models.CharField(max_length=255)

    def __str__(self):
        return self.squawk
