from django.db import models
from django.utils import timezone

class Post(models.Model):
    text = models.CharField(max_length=140)
    date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.text