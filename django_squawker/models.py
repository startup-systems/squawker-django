from django.db import models


class Posts(models.Model):
    text = models.CharField(max_length=140)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-date_time']
