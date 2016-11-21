from django.shortcuts import render
from django.http import HttpResponse

from .models import Squawk


def index(request):
    if request.method == 'POST':
        newSquawk = request.POST.get('new_squawk')
        if len(newSquawk) <= 140:
            newPost = Squawk(squawk_text=newSquawk)
            newPost.save()
    latest_squawk_list = Squawk.objects.order_by('-timestamp')[:20]
    context = {'latest_squawk_list': latest_squawk_list}
    return render(request, 'squawkerapp/index.html', context)
