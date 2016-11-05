from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

from .models import squawksPost
from .forms import squawkerAppForm


def index(request, pageN=0):
    pageN = int(pageN)
    if request.method == 'POST':
        form = squawkerAppForm(request.POST)
        if form.is_valid():
            s = squawksPost(msg=form.cleaned_data['msg'])
            s.save()
            return HttpResponseRedirect(reverse('squawkerapp:index'))
        else:
            return HttpResponseBadRequest("Invalid data")
    else:
        form = squawkerAppForm()

    squawks = squawksPost.objects.order_by('-id')

    return render(request, 'squawkerapp/index.html', {
        'squawks': squawks[pageN * 20:pageN * 20 + 20],
        'total': len(squawks),
        'form': form,
        'has_next': (len(squawks) > pageN * 20 + 20),
        'has_prev': (pageN > 0),
        'next_page': pageN + 1,
        'prev_page': pageN - 1
    })
