# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 09:39:03 2016

@author: Federico
"""

from django.http import HttpResponse
from squawker.models import Squawk
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    get_squawks = Squawk.objects.all().order_by('-time')
    context = {'get_squawks': get_squawks}

    return render(request, 'index.html', context)

@ensure_csrf_cookie

def postMsg(request):
    squawk_save = Squawk(text=request.POST['usr_message'])
    if len(squawk_save.text) > 140:
        response = HttpResponse('Invalid Input')
        response.status_code = 400
        return response
    squawk_save.save()
    return HttpResponseRedirect('/')
