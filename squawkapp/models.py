from django.db import models

class squawkText(models.Model):
    squawk_text = models.CharField(max_length=140)
    id = models.AutoField(primary_key=True)
    