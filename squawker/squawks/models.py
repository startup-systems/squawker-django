from django.db import models

# Create your models here.

class Squawks(models.Model):
    squawks_text = models.CharField(max_length=140)
    squawk_time = models.DateTimeField('Time', auto_now_add=True)

    def __str__(self):
        return self.squawks_text + ' time ' + str(squawk_time)

    class Meta:
        ordering = ['-squawk_time']
