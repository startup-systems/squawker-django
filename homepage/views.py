from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Mymessage


def index(request, nowpage='1'):
    post = request.POST.get('msg', False)
    if post:
        if len(post) > 140:
            return HttpResponseBadRequest()
        Mymessage(message_text=post).save()

    count = Mymessage.objects.all().count()
    if count != 0:
        lower = count - 20 * int(nowpage) + 1
        upper = count - 20 * (int(nowpage) - 1)
        allthemessage = Mymessage.objects.filter(message_id__gte=lower).filter(message_id__lte=upper).order_by("-message_id")
    else:
        allthemessage = []
    prevpage, nextpage = True, True
    if int(nowpage) == 1:
        prevpage = False
    if count - 20 * int(nowpage) + 1 < 0:
        nextpage = False

    context = {"allthepost": enumerate(allthemessage), "nowpageprev": int(nowpage) - 1, "nowpagenext": int(nowpage) + 1, "nowpageh": int(nowpage), "prev": prevpage, "nextp": nextpage}
    return render(request, 'homepage/index.html', context)
