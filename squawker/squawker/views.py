from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from .models import Squawks


def index(request):
    page = 1
    status = 200
    if request.method == 'GET' and len(request.GET) > 0:
        page = int(request.GET.get('page'))

    if request.method == 'POST' and len(request.POST) > 0:
        new_msg = request.POST.get('squawk_msg')
        if len(new_msg) <= 140:
            new_squawk = Squawks(msg=new_msg)
            new_squawk.save()
        else:
            status = 400

    template = loader.get_template('home.html')
    all_squawks = Squawks.objects.all()
    p_start = min(len(all_squawks) - 1, (page - 1) * 20)
    p_end = min(len(all_squawks), (page * 20))
    viewable_squawks = all_squawks[p_start:p_end]

    context = {'page': page, 'viewable_squawks': viewable_squawks, }
    if status == 400:
        return HttpResponseBadRequest(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))
