from django.db import models

# Create your models here.


class Squawk(models.Model):
    text = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
