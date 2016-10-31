from django.conf.urls import url
from . import views

app_name = 'squawker'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_squawker, name='add'),
]
