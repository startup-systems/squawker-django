from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, \
                        HttpResponseBadRequest
from django.urls import reverse

from .models import Squawk
from .forms import SquawkForm


def index(request):
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
    return render(request, 'squawk/index.html', {'squawks': squawks,
                  'total': len(squawks), 'form': form})
