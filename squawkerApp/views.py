from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from .models import Squawker
import pdb


def index(request):
    if request.method == 'POST':
        newMText = request.POST['message']
        if len(newMText) > 140:
            res = HttpResponse('text exceed 140 characters')
            res.status_code = 400
            return res
        newM = Squawker(message=newMText, pub_date=timezone.now())
        newM.save()
    # pdb.set_trace()
    latest_message_list = Squawker.objects.all().order_by('-pub_date')[:20]
    context = {
        'latest_message_list': latest_message_list,
    }
    return render(request, 'squawkerApp/index.html', context)


def next(request):
    other_message_list = Squawker.objects.order_by('-pub_date')[20:]
    context = {
        'other_message_list': other_message_list,
    }
    return render(request, 'squawkerApp/next.html', context)
