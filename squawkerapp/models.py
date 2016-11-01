from django.db import models

class postSquawk(models.Model):
    message=models.CharField(max_length=140)

