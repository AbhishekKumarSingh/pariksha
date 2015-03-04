from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from quiz.models import Question
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect

from braces import views
from models import UserResponse, Choice, Quiz


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'quiz/index.html'
    context_object_name = 'latest_quiz_list'

    def get_queryset(self):
        '''
                Return last five published question not including
                those which are to be published in future
        '       '''
        return Quiz.objects.filter(
            date_created__lte=timezone.now()).order_by('date_created')[:5]


# This view will add questions count and question iterator to user session
class QuizHomeView(generic.DetailView):
    """
         It renders detail view of a Quiz instance and
         add question sets related to Quiz instance
         to the user session.
        """
    template_name = 'quiz/startquiz.html'
    model = Quiz

    def get_object(self, queryset=None):
        obj = super(QuizHomeView, self).get_object()
        quiz = obj
        question_list = quiz.questions_list.all()
        question_list = question_list.order_by('id').reverse()
        question_id_list = [question.id for question in question_list]
        question_count = Question.objects.count()
        self.request.session['quest_count'] = question_count
        self.request.session['question_id_list'] = question_id_list
        self.request.session['quiz_max_score'] = quiz.maxPossibleScore()
        return obj


# TODO - if don't go on start and directly go to a question then problem
def next_view(request, pk):
    if 'question_id_list' in request.session:
        try:
            q_list = request.session['question_id_list']
            q_id = q_list.pop()
            request.session['question_id_list'] = q_list
        except IndexError:
            # Means I am done with all questions redirect to Result view.
            return redirect(reverse_lazy('quiz:result'))
        else:
            return redirect(reverse_lazy('quiz:detail', kwargs={'pk': q_id}))
    else:
        return Http404() # TODO - do something about this, if user visit next
        #  view without starting quiz it's fatal. fix this


class QuestionDetailView(
    views.LoginRequiredMixin,
    generic.DetailView
):
    template_name = 'quiz/detail.html'
    model = Question

    # def get_context_data(self, **kwargs):
    #     context = super(DetailView, self).get_context_data(**kwargs)
    #     context['desc'] = context['question'].question_desc
    #     return context


class UserResponseView(
    views.LoginRequiredMixin,
    generic.CreateView
):
    model = UserResponse

    def post(self, request, pk, *args, **kwargs):
        selected_choice = None
        if 'choice' in request.POST:
            selected_choice = Choice.objects.get(pk=request.POST['choice'])
        if selected_choice:
            question = selected_choice.question
            user = self.request.user
            # create a UserResponse Object and Save
            response = UserResponse(user=user, question=question,
                                    answer=selected_choice)
            if selected_choice.isAnswer:
                response.score = question.score_point
            response.save()
        else:
            question = Question.objects.get(pk=pk)
            # return render(self.request, 'quiz/detail.html',
            #               {'question':question, 'error_message':"You didn't "
            #                                                  "select a " \
            #                                        "choice"})
            return HttpResponseRedirect(reverse('quiz:detail', args=(pk)))
            # TODO - fix it so that the above should return an error_message
        return next_view(request, pk)


class ResultView(
    views.LoginRequiredMixin,
    generic.TemplateView
):
    template_name = 'quiz/result.html'

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        context['user_score'] = calculate_total_user_score(self.request)
        context['max_possible'] = self.request.session['quiz_max_score']
        return context


def calculate_total_user_score(request):
    user = request.user
    user_response_list = user.responses.all()
    total_score = sum([ur.score for ur in user_response_list])
    return total_score

