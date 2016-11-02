from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from .models import Posts
from datetime import datetime


def index(request):
    content = ''
    if request.method == 'POST':
        content = request.POST['input']
        if len(content) > 140:
            return HttpResponseBadRequest()
    Posts(post_text=content, post_time=datetime.now()).save()
    latest_posts = Posts.objects.order_by('-post_time')
    context = {'latest_posts': latest_posts}
    return render(request, 'tweet/index.html', context)
