from django.db import models

# Create your models here.


class Post(models.Model):
    content = models.TextField(max_length=140)
    timestamp = models.DateTimeField('time published')

    def __str__(self):
        return self.title
