from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db import models
from webapp.models import MyTable
from django.shortcuts import render_to_response
from django.views.decorators import csrf
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Add support for pagination
# References:
# https://www.tutorialspoint.com/
# http://www.w3schools.com/
# https://www.sitepoint.com/basic-jquery-form-validation-tutorial/
# http://opentechschool.github.io/python-flask/core/form-submission.html
# http://flask.pocoo.org/snippets/44/


# Create your views here.
def index(request, page=0):
    myList = ['One', 'Two', 'Three']
    # newComment = MyTable.objects.create(comment="This is the third comment!")
    # newComment.save()
    # myList = MyTable.objects.all()
    # myList = MyTable.objects.all().order_by('timestamp').latest()

    myList = MyTable.objects.all().order_by('-id')
    paginator = Paginator(myList, 2)    # Show 20 contacts per page

    page = request.GET.get('page')

    try:
        rows = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        rows = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        rows = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'rows': rows})
    #  return HttpResponse("<h2> Hello World </h2>")


def newComment(request, page=0):
    myList = ['One', 'Two', 'Three']

    # Process post variales
    if request.method == 'POST':
        value = request.POST['comment']
        print(value)

    if(len(value) < 2) or (len(value) > 140):
        # render(request, 'index.html', {'rows':myList})
        # return HttpResponse(status=400)
        myList = MyTable.objects.all().order_by('-id')
        return render(request, 'index.html', {'rows': myList}, status=400)
    else:
        newComment = MyTable.objects.create(comment=value)
        newComment.save()
        myList = MyTable.objects.all().order_by('-id')
        csrfContext = RequestContext(request)
        return redirect('/')
        # return render(request, 'index.html', {'rows':myList})
