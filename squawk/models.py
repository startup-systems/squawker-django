from django.db import models


class Squawk(models.Model):
    squawk = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.squawk + " " + self.pub_date.strftime("%B %d, %Y")
