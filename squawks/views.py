# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from squawks.models import Squawk


def index(request):
    squawks = Squawk.objects.order_by('-id')
    return render(request, "../templates/squawks/index.html", {'squawks': squawks})


def add_squawk(request):
    if request.method == 'POST':
        # TODO: Server side validation
        # if len(request.POST.get('squawk_text')) > 140:
        #     abort(400)
        s = Squawk(text=request.POST.get('squawk_text'))
        if len(s.text) <= 140:
            s.save()
        else:
            return HttpResponseBadRequest("/")
        return HttpResponseRedirect('/')
