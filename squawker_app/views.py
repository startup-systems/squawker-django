from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import RedirectView
from .models import Squawks


def index(request):
    latest_squawks = Squawks.objects.order_by('-id')
    context = {'latest_squawks': latest_squawks}
    return render(request, 'squawker_app/index.html', context)


def add_squawker(request):
    q = Squawks(squawks_text=request.POST['squawker'])
    if len(q.squawks_text) > 140:
        response = HttpResponse('Input should be less than 140 characters')
        response.status_code = 400
        return response
    q.save()
    return index(request)
