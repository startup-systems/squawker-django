from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.squawk_list, name='squawk_list'),
]
