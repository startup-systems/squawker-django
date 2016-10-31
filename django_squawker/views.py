from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .models import Posts
from django.views.decorators.csrf import ensure_csrf_cookie


def index(request):
    if request.method == 'POST':
        Posts.objects.create(text=request.POST['comment'])
        return redirect('/')
    latest_posts = Posts.objects.order_by('-date_time')[:5]
    template = loader.get_template('django_squawker/index.html')
    context = {
        'greeting_list': latest_posts,
        'prev_num': 0,
        'next_num': 0,
    }
    return HttpResponse(template.render(context, request))


def detail(request, page):
    return HttpResponse("You're looking at my_args %s." % page)
