#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'sidxiong'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post', views.post, name='post'),
]
