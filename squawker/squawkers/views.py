from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest
from django.template import RequestContext, loader

from .models import Posts
def index(request):
    if request.method == 'POST':
        newpost = request.POST.get('user_post')
        if len(newpost)>140:
            return HttpResponseBadRequest()
        else:
            p = Posts(post=newpost)
            p.save()
    post_list = Posts.objects.order_by("-post_id")
    context = {'post_list': post_list}
    return render(request,'squawkers/index.html',context)
