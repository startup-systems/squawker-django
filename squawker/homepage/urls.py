from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from homepage.models import Squawk

urlpatterns = [ url(r'^', ListView.as_view(queryset=Squawk.objects.all().order_by("-date"), template_name="homepage/home.html"))]