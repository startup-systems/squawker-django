from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post 
from .forms import NameForm
from django.views import generic
from django.urls import reverse

class IndexView(generic.ListView):
    template_name = 'squawker/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        #"""Return the last five published questions."""
        return Post.objects.order_by('-post_date')[:5]


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid()
            return HttpResponseRedirect('/')
    #if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'squawker/index.html', {'form': form})

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
