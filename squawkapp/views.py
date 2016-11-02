from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from .models import squawkText
from django.urls import reverse


def index(request):
    if (request.method == 'POST'):
        squawkcaption = request.POST['caption']
        if len(squawkcaption) > 140:
            return HttpResponseBadRequest()
        else:
            msg = squawkText(squawk_text=squawkcaption)
            msg.save()
            return HttpResponseRedirect(reverse('index'))
    result = squawkText.objects.order_by('-id')
    context = {'rows': result}
    return render(request, 'squawkapp/index.html', context)
