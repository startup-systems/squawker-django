from django.db import models


# Create your models here.
class Post(models.Model):
    squawk = models.CharField(max_length=140)
    post_date = models.DateTimeField()
