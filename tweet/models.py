from django.db import models


class postSquawks(models.Model):
    msg = models.CharField(max_length=140)
