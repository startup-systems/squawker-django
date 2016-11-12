from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from datetime import datetime


# Create your views here.
def index(request):
    page = request.GET.get('page', 1)
    if request.method == 'POST':
        if len(request.POST['content']) > 140:
            return HttpResponseBadRequest("400")
        else:
            Post.objects.create(squawk=request.POST['content'], post_date=datetime.now())
    posts_list = Post.objects.order_by('-post_date')[:]
    paginator = Paginator(posts_list, 20)
    try:
        posts_show = paginator.page(page)
    except PageNotAnInteger:
        posts_show = paginator.page(1)
    except EmptyPage:
        posts_show = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'feeds': posts_show})
