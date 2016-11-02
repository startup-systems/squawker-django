from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models import posts
import time

# Create your views here.

def index(request):
    if request.method == 'POST':
        post_msg = request.POST.get('get_posts')
        if len(post_msg) > 140:
            return HttpResponseBadRequest()
        else:
            t = time.time()
            newPost = posts(message=post_msg, post_time=t)
            newPost.save()
    squawkers = posts.objects.order_by('-post_time')[:20]
    context = {'squawkers': squawkers}
    return render(request, 'post/index.html', context)