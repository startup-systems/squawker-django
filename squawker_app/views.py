from django.http import HttpResponse, \
    HttpResponseBadRequest, \
    HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Squawk
from datetime import datetime

FORMAT = "%Y-%m-%d %H:%M:%S"
OUT_FORMAT = "%Y-%m-%d %H:%M:%S %Z"


def index(request):
    latest_squawk_list = Squawk.objects.order_by('ts').reverse()
    template = loader.get_template('base.html')
    context = {'items': [(item.post, item.ts.strftime(OUT_FORMAT)) for item in latest_squawk_list]}
    return HttpResponse(template.render(context, request))


def post(request):
    try:
        text = request.POST['input-post']
        if not (0 < len(text.rstrip()) <= 140):
            raise ValueError
    except (KeyError, ValueError):
        return HttpResponseBadRequest("Check your input.")
    else:
        created = Squawk.objects.create(post=text, ts=datetime.utcnow().strftime(FORMAT))
        print("[INFO:] Insert %s, %s" % (created.post, created.ts))
        return HttpResponseRedirect(reverse(index))
