from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse

from .models import Squawk
from .forms import SquawkForm


def index(request, page=0):
    if request.method == 'POST':
        form = SquawkForm(request.POST)
        if form.is_valid():
            s = Squawk(text=form.cleaned_data['text'])
            s.save()
            return HttpResponseRedirect(reverse('squawk:index'))
        else:
            return HttpResponseBadRequest("Invalid data")
    else:
        form = SquawkForm()

    squawks = Squawk.objects.order_by('-date')
    return render(request, 'squawk/index.html', {
        'squawks': squawks[int(page) * 20:int(page) * 20 + 20],
        'total': len(squawks),
        'form': form,
        'has_next': (len(squawks) > int(page) * 20 + 20),
        'next_page': int(page) + 1})
