# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 09:34:10 2016

@author: Federico
"""


from django.db import models


class Squawk(models.Model):
    text = models.CharField(max_length=140)
    time = models.TimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.text
        