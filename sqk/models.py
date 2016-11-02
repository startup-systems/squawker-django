from django.db import models


class posts(models.Model):
	message = models.CharField(max_length=140)
	post_time = models.FloatField()
