from django.shortcuts import render
from django.views.generic import ListView, DetailView
from homepage.models import Squawk

def index(request):
	return render(request, "homepage/home.html")