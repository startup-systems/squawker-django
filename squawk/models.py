from django.db import models

class Squawk(models.Model):
    text = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text
