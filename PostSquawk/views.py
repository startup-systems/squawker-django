from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .models import postSquawk
from django.shortcuts import render
from django.urls import reverse


def index(request):
    if (request.method == 'POST'):
        txt = request.POST['msg']
        if len(txt) <= 140:
            m = postSquawk(msg=txt)
            m.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseBadRequest(400)
    posts = postSquawk.objects.order_by('-id')
    return render(request, 'PostSquawk/index.html', {'squawks': posts})
