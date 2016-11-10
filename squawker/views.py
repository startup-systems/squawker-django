from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Squawks
'''



'''


test = []


def index(request):

    if request.method == 'POST':
        test.append(request.POST['name'])
        print test
        query = Squawks(squawk=request.POST['name'])
        query.save()
    resultList = list(Squawks.objects.all())

    return render(request, 'index.html', {'squawks': resultList[::-1]})
