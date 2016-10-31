from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import RedirectView
from .models import Squawks



# Create your views here.
def index(request):
	latest_squawks = Squawks.objects.order_by('-id')
	context = {'latest_squawks': latest_squawks}
	print("Printing This")
	return render(request, 'squawker_app/index.html', context)

def add_squawker(request):
	print ("I am here")
	q = Squawks(squawks_text=request.POST['squawker'])
	print (q)
	q.save()
	print ("Complete")
	#return render(request,"squawker_app/index.html")
	return index(request)