from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import RedirectView
from .models import Squawks


def index(request):
    context = {'past_squawks': Squawks.objects.order_by('-id')}
    return render(request, 'index.html', context)


def add_squawker(request):
    q = Squawks(squawk=request.POST['content'])
    if len(q.squawk) > 140:
        response = HttpResponse('Please enter less than 140 characters')
        response.status_code = 400
        return response
    q.save()
    return index(request)
