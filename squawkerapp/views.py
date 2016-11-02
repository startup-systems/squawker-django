from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from .models import postSquawk


def index(request):
    if request.method == 'POST':
        newSquawk = request.POST.get('content')
        # post length check
        if len(newSquawk) > 140:
            return HttpResponseBadRequest()
        else:
            newPost = postSquawk(message=newSquawk)
            newPost.save()
    squawks = postSquawk.objects.order_by('-id')
    return render(request, 'squawkerapp/index.html', {'squawks': squawks})
