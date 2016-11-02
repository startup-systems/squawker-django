from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from .models import Squawks
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def test(request):
    return HttpResponse(Squawks.objects.all())


def index(request):
    return redirect('page', page_num=1)


@csrf_exempt
def add(request):
    text = request.POST['new_body']
    if(len(text) > 140):
        return HttpResponseBadRequest('Not allowed')
    s = Squawks(squawk=request.POST['new_body'])
    s.save()
    return HttpResponseRedirect(reverse('index', ))


def page(request, page_num):
    page_num = int(page_num)
    top = page_num * 20
    bottom = (page_num - 1) * 20
    # Define page context
    squawk_list = Squawks.objects.order_by('-id')[bottom:top]
    if (len(squawk_list)):
        firstPage = True if page_num == 1 else False
        lastPage = True if squawk_list[len(squawk_list) - 1].id == 1 else False
    else:
        firstPage = lastPage = True;
    # Store page context
    context = {'squawks': squawk_list,
               'firstPage': firstPage,
               'lastPage': lastPage,
               'currPage': page_num}
    return render(request, 'index.html', context)
