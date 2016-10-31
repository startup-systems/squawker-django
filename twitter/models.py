from django.db import models


class postSqwaks(models.Model):
    msg = models.CharField(max_length=140)
