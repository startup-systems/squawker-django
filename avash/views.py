from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from avash.models import Squawk


def index(request):
    start = request.GET.get('start') or 0
    start = int(start)

    squawks = Squawk.objects.order_by('-id')[start:start + 20]
    count = Squawk.objects.count()

    trigger = 0
    if start / 20 < (count / 20) - 1:
        trigger = 1

    start += 20
    return render(request, 'squawker/index.html', {'squawks': squawks, 'start': start, 'trigger': trigger})


def add_squawk(request):
    if request.method == "POST":
        s_text = request.POST.get('squawkText')

        if len(s_text) > 140:
            errorResponse = HttpResponse('the limit is 140 bro')
            errorResponse.status_code = 400
            return errorResponse
        else:
            s = Squawk(text=s_text)
            s.save()

    return HttpResponseRedirect('/')
