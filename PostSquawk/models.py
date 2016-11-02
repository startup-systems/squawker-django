from django.db import models


class postSquawk(models.Model):
    msg = models.CharField(max_length=140)
# Create your models here.
