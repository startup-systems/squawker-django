from django.db import models


class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    post = models.CharField(max_length=140)
 
def __str__(self):
        return self.post
