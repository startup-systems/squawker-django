from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Post
from datetime import datetime
# Create your views here.


def post_list(request):
    content = ''
    if request.method == "POST":
        content = request.POST['input']
        if len(content) > 140:
            return HttpResponseBadRequest()
        else: 
            Post(content=content, timestamp=datetime.now()).save()
    queryset = Post.objects.all().order_by('-id')
    context = {
        "obj_lists": queryset,
        "title": "Squawker",
        }
    return render(request, "index.html", context)
