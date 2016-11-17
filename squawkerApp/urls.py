from django.conf.urls import url

from . import views

# app_name = 'squawkerApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
