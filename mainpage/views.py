from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
import time


def index(request):
    MAX_POSTS = 20
    if request.method == 'POST':
        post = request.POST['text_box_input']
        if len(post) > 140:
            response = HttpResponse('Invalid input length (must be less than 140)')
            response.status_code = 400
            return response
        t = time.time()
        Posts(message=post, post_time=t).save()
    latest_posts = Posts.objects.order_by('-post_time')[:MAX_POSTS]
    context = {'latest_posts': latest_posts}
    return render(request, 'mainpage/index.html', context)
