from django.db import models

import datetime


from django.utils import timezone


# Create your models here.


class squawker(models.Model):
    squawk = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.squawk

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
