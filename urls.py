from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PostView.as_view(), name='post_list')
]
