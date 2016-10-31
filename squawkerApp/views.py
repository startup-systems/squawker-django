from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from django.urls import reverse

from .models import Squawk

# Create your views here.


def index(request):
    if(request.method == 'POST'):
        post_text = request.POST['post_text']
        if(len(post_text) > 140):
            return HttpResponseBadRequest("Squawk too long!")
        else:
            s = Squawk(text=post_text)
            s.save()
            return HttpResponseRedirect(reverse('index'))
    squawks = Squawk.objects.order_by('-id')
    context = {'squawks': squawks}
    return render(request, 'squawkerApp/index.html', context)
