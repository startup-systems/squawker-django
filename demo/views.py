# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseBadRequest
from django.template import loader
from django.views import defaults

from .models import Squawk


def index(request, page_id="1"):
    if len(request.POST) > 0:
        s = request.POST['squawk']
        print(s)
        print(len(s))
        if len(s) > 140:
            return HttpResponseBadRequest()

        t = Squawk(squawk_text=request.POST['squawk'], pub_date=timezone.now())
        t.save()

    pageN = int(page_id)
    squawk_list = Squawk.objects.order_by('-pub_date')
    numSquawks = len(squawk_list)
    squawk_list = squawk_list[(pageN - 1) * 20: min(numSquawks, pageN * 20)]
    haveNext = 0
    havePre = 0

    if pageN > 1:
        havePre = 1

    if pageN * 20 < numSquawks:
        haveNext = 1

    context = {
        'squawk_list': squawk_list,
        'pageN': pageN,
        'numSquawks': numSquawks,
        'haveNext': haveNext,
        'havePre': havePre,
    }
    return render(request, 'demo/index.html', context)
