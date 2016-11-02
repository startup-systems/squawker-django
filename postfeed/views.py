from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from .models import Post
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    if (request.method == 'POST'):
        msgText = request.POST['msg']
        length = len(msgText)
        if length > 140:
            return HttpResponseBadRequest()
        else:
            m = Post(msg=msgText)
            m.save()
            return HttpResponseRedirect(reverse('index'))
    result = Post.objects.order_by('-auto_id')
    context = {'rows': result}
    return render(request, 'index.html', context)

# Create your views here.
