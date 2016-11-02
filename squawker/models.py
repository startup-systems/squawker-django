from django.db import models


class Squawks(models.Model):
    squawk = models.CharField(max_length=140)
