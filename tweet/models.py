from django.db import models


class postSquawks(models.Model):
    msg = models.TextField(max_length=140)
