from django.conf.urls import url

from . import views

app_name = 'tweet'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pageNumber>[0-9]+)$', views.index, name='index'),
]
