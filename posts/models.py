from django.db import models


class Squawkers(models.Model):
    squawkers_text = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date published')
