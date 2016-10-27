from django.shortcuts import render, redirect
from django.http import HttpResponse
from squawker.models import Squawk

# from models import Squawks

# Create your views here.
def index(request):
    context = "yo"
    squawks = Squawk.objects.order_by('id')
    return render(request, 'squawker/index.html', {"squawks": squawks})

def add_squawk(request, text):
    context = "yo"
    # if len(request.form['squawk_text']) > 140:
    #     abort(400)
    # use this https://docs.djangoproject.com/en/1.10/topics/forms/
    s = Squawk(text='yo')
    s.save()
    # create db connection and store the squawk
    return render(request, 'squawker/index.html')
