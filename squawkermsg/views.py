from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone


# def index(request):
#     return HttpResponse("Hello, world. Page to input and show tweets.")


from .models import squawker


# def index(request):
#     latest_question_list = squawker.objects.order_by('-pub_date')
#     output = ', '.join([q.squawk for q in latest_question_list])
#     return HttpResponse(output)


def index(request):
    if request.method == 'POST':
        squawk2 = request.POST['message']
        print(squawk2)
        if len(squawk2) > 140:
            res = HttpResponse('text exceed 140 characters')
            res.status_code = 400
            return res
        msg = squawker(squawk=squawk2, pub_date=timezone.now())
        print("squawk is " + msg.squawk)
        msg.save()
    # pdb.set_trace()
    latest_question_list = squawker.objects.all().order_by('-pub_date')
    print(latest_question_list)
    # p=[]
    # for i in latest_question_list:
    # 	print("New squakkd "+i.squawk)
    # 	p.append(i.squawk)
    # blah = iter([q.squawk for q in latest_question_list])
    context = {'latest_question_list': latest_question_list}
    return render(request, 'squawkermsg/index.html', context)

# Leave the rest of the views (detail, results, vote) unchanged
