from django.db import models

# Create your models here.


class posts(models.Model):
    msg_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=140)
