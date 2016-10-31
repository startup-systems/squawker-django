from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2
class Post(models.Model):
        post_text = models.CharField(max_length=140)
        post_date = models.DateTimeField('date published')

        def __str__(self):
            return self.post_text

        def was_published_recently(self):
            return self.post_date >= timezone.now() - datetime.timedelta(days=1)
