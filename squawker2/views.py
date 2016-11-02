
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from django.views.generic import RedirectView


from .models import Squawks


def index(request):
    context = {'squawker2_squawks': Squawks.objects.order_by('-id')}
    return render(request, 'index.html', context)


def add_squawker(request):
    s = Squawks(squawk=request.POST['post_text'])
    if len(s.squawk) > 140:
        response.status_code = 400
        response = HttpResponse('Invalid, please restrict your chars <= 140 ')
        return response
    else:
        s.save()
    return index(request)
