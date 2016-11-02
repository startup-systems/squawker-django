# encoding: utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from main.models import Squawk

# Create your views here.

def index(request):
    if request.method == "POST":
        text = request.POST["text"]
        if len(text)>140:
            return HttpResponseBadRequest("LENGHT OF TEXT BIGGER THAN 140!")
        squawk = Squawk(message=text)
        squawk.save()
        return redirect(index)
    else:
        squawks = Squawk.objects.all()
        return render(request, "show_entries.html", {"entries":squawks})    
    
