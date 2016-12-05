from django.db import models


class postSquawk(models.Model):
	auto_id = models.AutoField(primary_key=True)
	message = models.CharField(max_length=140)
