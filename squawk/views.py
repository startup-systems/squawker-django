from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Squawk


def index(request):
    if request.method == 'POST':
        squawk_text = request.POST['squawk']
        if (squawk_text != "") and (len(squawk_text) <= 140):
            s = Squawk(squawk=squawk_text, pub_date=timezone.now())
            s.save()
    return render(request, 'squawk/index.html', {"squawks": Squawk.objects.order_by('-pub_date')})
