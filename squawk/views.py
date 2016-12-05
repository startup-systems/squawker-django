from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from .models import postSquawk
from django.urls import reverse

def index(request):
    if request.method == 'POST':
        msg = request.POST.get('message')
        # post length check
        if len(msg) > 140:
            return HttpResponseBadRequest()
        else:
            newPost = postSquawk(message=msg)
            newPost.save()
    squawkers = postSquawk.objects.order_by('-auto_id')
    return render(request, 'index.html', {'squawks': squawkers})
