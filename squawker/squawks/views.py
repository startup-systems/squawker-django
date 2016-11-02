from django.shortcuts import render
from django.http import HttpResponse
from .models import Squawks

def index(request):
    if request.method == 'POST':
        message = request.POST['squawk']
        if len(message) > 140:
            return HttpResponse(status=400)
        elif len(message) > 0:
            new_squawk = Squawks(squawks_text=message)
            new_squawk.save()
    all_squawks = Squawks.objects.all()
    
    return render(request, 'index.html', {'all_squawks': all_squawks})
