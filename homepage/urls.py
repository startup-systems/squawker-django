from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<nowpage>[0-9]+)/$', views.index, name="indexw"),
    url(r'^$', views.index, name='index'),
]
