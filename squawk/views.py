from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Squawk
from .forms import SquawkForm
import time
from math import ceil

ENTRIES_PER_PAGE = 20

def index(request, num="1"):
    num=int(num)
    status=200
    if request.method == 'POST':
        form = SquawkForm(request.POST)
        if form.is_valid():
            s = Squawk(message=form.cleaned_data['message'], create_at=int(time.time()))
            s.save()
        else:
            status=400
    else:
        form = SquawkForm()

    last_page = ceil(Squawk.objects.count() / ENTRIES_PER_PAGE)
    offset = ENTRIES_PER_PAGE * (num-1)
    limit = offset + ENTRIES_PER_PAGE

    squawkers = Squawk.objects.order_by('-create_at')[offset:limit]

    if num > last_page+1:
        raise Http404("Page does not exist")

    context = {
        'squawkers': squawkers,
        'prev': num-1,
        'page': num,
        'next': num+1,
        'last_page': last_page,
        'form':form
    }
    return render(request, 'squawk/index.html', context, status=status)
