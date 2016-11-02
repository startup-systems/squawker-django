from django.shortcuts import render
from django.http import HttpResponse
from .models import posts
import time
# Create your views here.
def index(request):
    if request.method == 'POST':
        post_msg = request.POST['get_posts']
        if len(post_msg) > 140:
            response = HttpResponse('Your squawker should be less than 140 characters.')
            response.status_code = 400
            return response
        t = time.time()
        posts(message=post_msg, post_time=t).save()
    new_posts = posts.objects.order_by('-post_time')[:20]
    context = {'new_posts': new_posts}
    return render(request, 'post/index.html', context)