from django.db import models


class Squawk(models.Model):
	post = models.CharField(max_length=140)
	timestamp = models.FloatField()
