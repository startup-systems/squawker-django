from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from squawker_django.models import Squawk


def index(request):
    squawks = Squawk.objects.order_by('-id')
    for i in squawks:
        print(i.text)
    return render(request, 'squawker/index.html', {'squawks': squawks})


def add_squawk(request):
    if request.method == "POST":
        s_text = request.POST.get('squawk_text')

        if len(s_text) > 140:
            errorResponse = HttpResponse('Input is too long, cannot be greater than 140 characters')
            errorResponse.status_code = 400
            return errorResponse
        else:
            s = Squawk(text=s_text)
            s.save()

    # Send user back to homepage
    return HttpResponseRedirect('/')
