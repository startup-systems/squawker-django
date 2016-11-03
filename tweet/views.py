from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

from .models import postSquawks
from .forms import squawkForm


def index(request, page=0):
    pageNumber = int(page)
    if request.method == 'POST':
        form = squawkForm(request.POST)
        if form.is_valid():
            s = postSquawks(msg=form.cleaned_data['msg'])
            s.save()
            return HttpResponseRedirect(reverse('tweet:index'))
        else:
            return HttpResponseBadRequest("Invalid data")
    else:
        form = squawkForm()

    squawks = postSquawks.objects.order_by('-id')

    return render(request, 'tweet/index.html', {
        'squawks': squawks[pageNumber * 20:pageNumber * 20 + 20],
        'total': len(squawks),
        'form': form,
        'has_next': (len(squawks) > pageNumber * 20 + 20),
        'has_prev': (pageNumber > 0),
        'next_page': pageNumber + 1,
        'prev_page': pageNumber - 1
    })
