from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import postSquawk

def index(request):
    if request.method == 'POST':
        newSquawk=request.POST.get('content')
	# post length check
        if len(newSquawk) > 140:
            return "Input should be less than 140 characters!", 400
        else:
            newPost=postSquawk(message=newSquawk)
            newPost.save()
    squawks=postSquawk.objects.order_by('-id')  
    return render(request,'squawkerapp/index.html',{'squawks':squawks})

