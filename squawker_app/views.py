from django.shortcuts import render
from django.http import HttpResponse
from .models import Squawker
# Create your views here.


def index(request):
    if request.method == "POST":
        message = request.POST["squawkerMessage"]
        if len(message) > 140:
        	error = "Please enter the message that the maximum length should be less than 140 characters"
        	return HttpBadResponse('400')
        else:
            msg = Squawker(post=message)
            msg.save()
    postMsg = Squawker.objects.order_by('id').reverse()[0:20]
    context = {'postMsg': postMsg}
    return render(request, 'index.html', context)