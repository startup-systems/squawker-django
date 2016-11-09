from django.db import models


class Squawk(models.Model):
    txt = models.CharField(max_length=140)
    date = models.DateTimeField()

    def __str__(self):
        return self.txt
