from django.db import models

# Create your models here.
# fix climated control + 100010
from django.db import models


class Squawks(models.Model):
    squawk = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.squawk
