from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from avash.models import Squawk


def index(request):
    squawks = Squawk.objects.order_by('-id')
    for i in squawks:
        print(i.text)
    return render(request, 'squawker/index.html', {'squawks': squawks})


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
