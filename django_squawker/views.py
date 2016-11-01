from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
# Create your views here.
from .models import Posts
from django.views.decorators.csrf import ensure_csrf_cookie


def index(request):
    if request.method == 'POST':
        if len(request.POST['comment']) > 140:
            return HttpResponseBadRequest("Bad input")
        Posts.objects.create(text=request.POST['comment'])
        return redirect('/')
    latest_posts = Posts.objects.order_by('-date_time')[:]
    template = loader.get_template('django_squawker/index.html')
    context = {
        'greeting_list': latest_posts,
        'next_num': 0,
    }
    return HttpResponse(template.render(context, request))


def detail(request, page):
    if request.method == 'POST':
        if len(request.POST['comment']) > 140:
            return HttpResponseBadRequest("400: Bad input")
        Posts.objects.create(text=request.POST['comment'])
        return redirect('/')
    latest_posts = Posts.objects.order_by('-date_time')[:]
    hasNextPage = 0
    if len(latest_posts) - (int(page) * 20) > 0:
        hasNextPage = 1
    template = loader.get_template('django_squawker/index.html')
    context = {
        'greeting_list': latest_posts[(int(page) - 1) * 20:int(page) * 20],
        'next_num': int(page) + 1,
        'hasNextPage': hasNextPage,
    }
    return HttpResponse(template.render(context, request))
