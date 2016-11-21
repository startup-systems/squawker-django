from django.db import models

# Create your models here.
class Squawker(models.Model):
	postmsg = models.CharField(max_length=140)
    
