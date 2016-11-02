from django.db import models


class Squawk(models.Model):
    squawk_text = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.squawk_text
