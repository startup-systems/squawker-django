from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Squawker


def index(request):
    if request.method == 'POST':
        scontent = request.POST['squawker_info']
        if len(scontent) > 140:
            errormsg = "The maximum length of the squawker should be 140"
            return HttpResponse(errormsg, status=400)
        else:
            sqs = Squawker(content=scontent)
            sqs.save()
    squawker_list = Squawker.objects.order_by('id').reverse()
    context = {'squawker_list': squawker_list}
    return render(request, 'index.html', context)
