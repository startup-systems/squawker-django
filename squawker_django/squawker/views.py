from django.shortcuts import render
from django.http import HttpResponse
from squawker.models import Squawk

# from models import Squawks

# Create your views here.
def index(request):
    context = "yo"
    squawks = Squawk.objects.order_by('id')
    return render(request, 'squawker/index.html', {"context": squawks})

def add_squawk(request):
    context = "yo"
    return render(request, 'squawker/index.html', {"context": context})
