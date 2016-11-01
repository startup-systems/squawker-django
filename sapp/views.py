from django.shortcuts import render
from django.http import HttpResponse
from .models import posts
import time


def index(request):
    if request.method == 'POST':
        post = request.POST['getPosts']
        if len(post) > 140:
            response = HttpResponse('Your post should be less than 140 characters.')
            response.status_code = 400
            return response
        t = time.time()
        posts(message=post, post_time=t).save()
    newPosts = posts.objects.order_by('-post_time')[:20]
    viewPosts = {'newPosts': newPosts}
    return render(request, 'sapp/index.html', viewPosts)
