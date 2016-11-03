from django.shortcuts import render
from django.http import HttpResponse
from .models import Squawk

# Create your views here.
def index(request):
	if request.method == 'POST':
		newsquawktext = request.POST['content']
		print(newsquawktext)

		if len(newsquawktext) > 140:
			pass #should throw error code 400

		newsquawk = Squawk(text=newsquawktext)
		newsquawk.save()

	squawks = Squawk.objects.order_by("-timestamp")
	return render(request, "front.html", {squawks: squawks})
