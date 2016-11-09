from django.db import models


class postSquawk(models.Model):
    msg = models.CharField(max_length=140)

    def __str__(self):
        return self.msg
# Create your models here.
