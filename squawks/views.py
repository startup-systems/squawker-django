from django.shortcuts import render
from squawks.models import Squawk


def squawk_list(request):
    squawks = Squawk.objects.all().order_by('created_date')
    return render(request, 'squawks/squawks_list.html', {'squawks': squawks})
