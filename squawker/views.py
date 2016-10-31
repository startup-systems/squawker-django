from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import SquawkForm
from django.views import generic
from django.urls import reverse
import datetime


def index(request):
    squawks = Post.objects.order_by('-post_date')
    return render(request, 'squawker/index.html', {'squawks': squawks})


def add_squawk(request):
    if request.method == 'POST':
        s = Post(post_text=request.POST.get('squawk_text'), post_date=datetime.datetime.now())
        s.save()
        return HttpResponseRedirect('/')
