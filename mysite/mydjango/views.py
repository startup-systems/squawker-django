from django.shortcuts import render
from django.http import HttpResponse
from .models import Squawker

# Create your views here.
def index(request):
    if request.method == "POST":
        new_message = request.POST["usr_message"]
        if len(new_message) > 140:
            return HttpResponse('Your message should be less than 140 characters.', status=400)
        else:
            message = Squawker(post=new_message)
            message.save()
    posts = Squawker.objects.order_by('id').reverse()[0:20]
    context = {'posts': posts}
    return render(request,'index.html', context)