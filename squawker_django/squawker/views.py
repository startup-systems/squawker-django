from django.shortcuts import render
from django.http import HttpResponse

# from models import Squawks

# Create your views here.
def index(request):
    context = "yo"
    return render(request, 'squawker/index.html')
