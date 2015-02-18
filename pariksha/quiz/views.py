from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from quiz.models import Question
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'quiz/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        '''
        Return last five published question not including
        those which are to be published in future
        '''
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]

class DetailView(generic.DetailView):
    template_name = 'quiz/detail.html'
    model = Question

    def get_context_data(self):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['desc'] = context['question'].question_desc
        return context

class ResultView(generic.DetailView):
    model = Question
    template_name = 'quiz/result.html'
