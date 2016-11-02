from django.shortcuts import render
from django.http import HttpResponseBadRequest
from squawks.models import Squawk
from .forms import SquawkForm


def squawk_list(request):

    def get_squawk_list(request):
        squawks = Squawk.objects.all().order_by('-created_date')
        return render(request, 'squawks/squawks_list.html', {'squawks': squawks})

    if request.method == 'POST':
        form = SquawkForm(request.POST)
        if form.is_valid():
            squawk = form.save()
        else:
            return HttpResponseBadRequest()
        return get_squawk_list(request)
    else:
        return get_squawk_list(request)
