from django.conf.urls import url

from . import views

app_name = 'squawkerapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pageN>[0-9]+)$', views.index, name='index'),
]
