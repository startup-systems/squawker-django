from django.db import models

class Mymessage(models.Model):
	message_id = models.AutoField(primary_key = True)
	message_text = models.CharField(max_length = 140)

	
