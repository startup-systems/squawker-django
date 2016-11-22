from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from squawker.models import Squawk
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from squawker.forms import SquawkForm


SQUAWKS_PER_PAGE = 20


def index(request, num=1):
    squawk_list = Squawk.objects.order_by('-id')
    paginator = Paginator(squawk_list, SQUAWKS_PER_PAGE)
    page = num
    try:
        squawks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        squawks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        squawks = paginator.page(paginator.num_pages)

    return render(request, 'squawker/index.html', {'squawks': squawks})


def add_squawk(request):
    if request.method == 'POST':
        # TODO: Server side validation
        if len(request.POST.get('squawk_text')) > 140:
            response = HttpResponse('Invalid input length (must be less than 140)')
            response.status_code = 400
            return response
        # Use django ORM api to store squawk
        else:
            s = Squawk(text=request.POST.get('squawk_text'))
            s.save()
    return HttpResponseRedirect('/')
