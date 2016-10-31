from django.conf.urls import url
from . import views

app_name = 'squawker'
urlpatterns = [url(r'^$', views.index, name='index'), url(r'^add-squawk/', views.add_squawk, name='index'),]
