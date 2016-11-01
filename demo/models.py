from django.db import models

# Create your models here.


class Squawk(models.Model):
    squawk_text = models.CharField(max_length=141)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.squawk_text
