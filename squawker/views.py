from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import SquawkForm
from django.views import generic
from django.urls import reverse
import datetime

#class IndexView(generic.ListView):
    #template_name = 'squawker/index.html'
    #context_object_name = 'latest_question_list'
    #def get_queryset(self):
        #return Post.objects.order_by('-post_date')[:5]
def index(request):
    squawks = Post.objects.order_by('-post_date')
    return render(request, 'squawker/index.html', {'squawks': squawks})

def add_squawk(request):
    if request.method == 'POST':
        s = Post(post_text=request.POST.get('squawk_text'), post_date=datetime.datetime.now())
        s.save()
        return HttpResponseRedirect('/')

'''
class IndexView(generic.ListView):
    template_name = 'squawker/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        #"""Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'squawker/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'squawker/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'squawker/detail.html', { 'question': question, 'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('squawker:results', args=(question.id,)))
    '''
