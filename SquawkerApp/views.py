from django.shortcuts import render, redirect
from .models import Squawks
from django.template import loader
from django.http import HttpResponse, HttpResponseBadRequest
from datetime import datetime


def index(request):
    allRows = Squawks.objects.order_by('-submitTime')
    template = loader.get_template('SquawkerApp/index.html')
    allSquawks = []
    for s in allRows:
        allSquawks.append(s.squawks)
    context = {'allsquawks': allSquawks}
    return HttpResponse(template.render(context, request))


def submitNewSquawk(request):
    newSquawk = request.POST['squawk']
    time = str(datetime.now())
    s = Squawks(submitTime=time, squawks=newSquawk)
    if len(newSquawk) > 140:
        return HttpResponseBadRequest('Squawk is longer than 140 characters!')
    s.save() 
    return redirect('index')
