from django.conf.urls import url

from . import views

app_name = 'squawk'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<page>[0-9]+)$', views.index, name='index'),
]
