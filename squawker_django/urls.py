from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.save_squawker, name='postSq'),
    url(r'^(?P<page_id>[0-9]+)/$', views.index, name='index'),
]

