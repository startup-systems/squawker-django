from django.db import models

class Post(models.Model):
    auto_id = models.AutoField(primary_key=True)
    msg = models.CharField(max_length=140)
# Create your models here.
