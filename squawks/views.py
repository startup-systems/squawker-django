from django.shortcuts import render

# Create your views here.
def squawk_list(request):
    return render(request, 'squawks/squawks_list.html', {})
