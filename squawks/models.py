from django.db import models
from django.utils import timezone

# Create your models here.

class Squawk(models.Model):
    text = models.TextField(max_length=140)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
