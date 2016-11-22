from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

from .models import postSquawks
from .forms import squawkerForm


def index(request, pageN=0):
    pageN = int(pageN)
    if request.method == 'POST':
        form = squawkerForm(request.POST)
        if form.is_valid():
            s = postSquawks(msg=form.cleaned_data['msg'])
            s.save()
            return HttpResponseRedirect(reverse('mywebapp:index'))
        else:
            return HttpResponseBadRequest("Invalid data")
    else:
        form = squawkerForm()

    squawks = postSquawks.objects.order_by('-id')

    return render(request, 'mywebapp/index.html', {
        'squawks': squawks[pageN * 20:pageN * 20 + 20],
        'total': len(squawks),
        'form': form,
        'has_next': (len(squawks) > pageN * 20 + 20),
        'has_prev': (pageN > 0),
        'next_page': pageN + 1,
        'prev_page': pageN - 1
    })

# Create your views here.
