from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic import RedirectView
from .models import Squawk


def index(request):
    object_list = {'All_squawks': Squawk.objects.order_by('-date')}
    return render(request, 'homepage/home.html', object_list)


def squawker(request):
    q = Squawk(txt=request.POST['content'])
    if len(q.txt) > 140:
        response = HttpResponse('Enter only 140 characters')
        response.status_code = 400
        return response
    q.save()
    return index(request)
