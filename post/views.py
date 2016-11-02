from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models import posts

# Create your views here.


def index(request):
    if request.method == 'POST':
        post_msg = request.POST['get_posts']
        if len(post_msg) > 140:
            return HttpResponseBadRequest()
        else:
            newPost = posts(message=post_msg)
            newPost.save()
    squawkers = posts.objects.order_by('-auto_id')
    context = {'squawkers': squawkers}
    return render(request, 'post/index.html', context)
