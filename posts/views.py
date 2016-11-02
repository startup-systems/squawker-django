from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Squawkers
from datetime import datetime


def index(request):
    if request.method == 'POST':
        squawks = request.POST.get("squawks")
        if len(squawks) > 140:
            return HttpResponseBadRequest()
        else:
            q = Squawkers(squawkers_text=squawks, pub_date=datetime.now())
            q.save()
    q_all = Squawkers.objects.order_by('-pub_date')[:20]
    return render(request, 'posts/index.html', {'squawkss': q_all})
