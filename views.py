from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.http import HttpResponseBadRequest
from django.views.generic import View

class PostView(View):
	def get(self, request, *args, **kwargs):
		posts = Post.objects.filter(date__lte=timezone.now()).order_by('-date')
		return render(request, 'postMachine/post_list.html', {'posts':posts}) #here
     
	def post(self, request, *args, **kwargs):
	
		text = request.POST.get('msg')
		if len(text)>140:
			return HttpResponseBadRequest()
		post = Post(text=text)
		post.save()
		posts = Post.objects.filter(date__lte=timezone.now()).order_by('-date')
		return render(request, 'postMachine/post_list.html', {'posts':posts}) #here
