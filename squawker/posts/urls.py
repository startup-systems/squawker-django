
from django.conf.urls import url
from django.contrib import admin
from . import views as posts_views

urlpatterns = [
    url(r'^$', posts_views.post_list, name="post_list"),
]
