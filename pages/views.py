from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Squawker

def index(request, page_id = 1):
	latest_squawker_list = Squawker.objects.order_by('-created_date')
	cnt = len(latest_squawker_list)
	template = loader.get_template('pages/index.html')
	_start = (int(page_id) - 1) * 20
 	_end = min(len(latest_squawker_list), (int(page_id) - 1) * 20 + 20)
	context = { 
		'msgs': latest_squawker_list[_start:_end],
		'page': int(page_id),
		'num': cnt
	}
	return HttpResponse(template.render(context, request))


def save_squawker(request):
	if(request.method == 'POST'):
		if len(request.POST['msg']) > 140:
			response = HttpResponse('Squawker too long')
			response.status_code = 400
			return response
		u = Squawker(squawker_msg = request.POST['msg'])
		u.save()
	return HttpResponseRedirect('/')

