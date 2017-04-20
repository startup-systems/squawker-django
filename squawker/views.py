from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect

from .models import Squawk

MAX_LEN = 140

def index(request):
    squawks = Squawk.objects.order_by('-pub_date').all()

    return render(request, "base.html",
                 {'title':"Squawk Posted",
                  'max_len':MAX_LEN,
                  'squawks':squawks
                 })


def isValid(squawk):
    return (len(squawk) <= MAX_LEN) and len(squawk) > 0


def post(request):
    # raise Http400("Question does not exist")
    posted_text=request.POST['squawk']
    if(isValid(posted_text)):
        s = Squawk(squawk_text=posted_text)
        s.save()
        return redirect(index)
    else:
        return HttpResponseBadRequest()
