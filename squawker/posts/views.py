from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    queryset = Post.objects.all().order_by('-id')
    context = {
        "obj_lists":queryset,
        "title":"Squawker",
        "form":form }
    return render(request, "index.html", context)







