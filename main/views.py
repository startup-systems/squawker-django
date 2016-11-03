# encoding: utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.paginator import Paginator
from main.models import Squawk

# Create your views here.
COUNT = 20

def index(request):
    page_number = 1
    if "page" in request.GET:
        page_number = int(request.GET["page"])
    
    if request.method == "POST":
        text = request.POST["text"]
        if len(text)>140:
            return HttpResponseBadRequest("LENGHT OF TEXT BIGGER THAN 140!")
        squawk = Squawk(message=text)
        squawk.save()
        return redirect(index)
    else:
        squawks = Squawk.objects.order_by('-time')
        p = Paginator(squawks, COUNT)
        page = p.page(page_number)
        objects = page.object_list
        return render(request, "show_entries.html", {"entries":objects, "has_previous":page.has_previous(), "has_next":page.has_next(), "page":page_number})
    
