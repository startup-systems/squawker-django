import time
from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
def index(request):
    if request.method == 'POST':
        post = request.POST['text_box_input']
        if len(post) > 140:
            response = HttpResponse('cannot exceed 140 characters)')
            response.status_code = 400
            return response
        t = time.time()
        Posts(message=post, timestamp=t).save()
    maxP = 20
    feed = Posts.objects.order_by('-timestamp')[:maxP]
    context = {'feed': feed}
    return render(request, 'main/index.html', context)
    