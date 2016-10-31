from django.db import models


class Squawk(models.Model):
    text = models.CharField(max_length=140)

    def __str__(self):
        return self.text
