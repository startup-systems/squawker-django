from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from squawker.models import Squawk
# from squawker.forms import SquawkForm

def index(request):
    squawks = Squawk.objects.order_by('-id')
    return render(request, 'squawker/index.html', {'squawks': squawks})


def add_squawk(request):
    if request.method == 'POST':
        # TODO: Server side validation
        # if len(request.POST.get('squawk_text')) > 140:
        #     abort(400)
        # Use django ORM api to store squawk
        s = Squawk(text=request.POST.get('squawk_text'))
        s.save()
    return HttpResponseRedirect('/')
