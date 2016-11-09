from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from homepage.models import Squawk


app_name = 'homepage'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.squawker, name='home'),
]
