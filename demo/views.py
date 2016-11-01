# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseBadRequest
from django.template import loader
from django.views import defaults

from .models import Squawk


def index(request, page_id = 0):
    if len(request.POST) > 0:
        s = request.POST['squawk']
        if len(s) == 0 or len(s) > 140:
            errorResponse = HttpResponse('Input is invalied')
            errorResponse.status_code = 400
            return errorResponse

        t = Squawk(squawk_text=request.POST['squawk'], pub_date=timezone.now())
        t.save()

    squawk_list = Squawk.objects.order_by('-pub_date')
    context = {
        'squawk_list': squawk_list,
        'page_id': page_id,
    }
    return render(request, 'demo/index.html', context)

