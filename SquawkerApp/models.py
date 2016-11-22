from django.db import models


class Squawks(models.Model):
    submitTime = models.DateTimeField('datetime published')
    squawks = models.CharField(max_length=140)
