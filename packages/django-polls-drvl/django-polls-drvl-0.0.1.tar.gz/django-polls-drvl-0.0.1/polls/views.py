from re import template
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.db.models import Count

from polls.models import Choice, Question


# Version 1
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = { 'latest_question_list': latest_question_list }
#     # output = '<br>'.join([q.question_text for q in latest_question_list])
#     return HttpResponse(template.render(context, request))

# Version 2
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = { 'latest_question_list': latest_question_list }
#     return render(request, 'polls/index.html', context)

# Version 3
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five questions posted with answer options."""
        qs = Question.objects.all()
        qs = qs.annotate(Count('choices'))
        qs = qs.filter(pub_date__lte=timezone.now())
        qs = qs.filter(choices__count__gt=0)
        return qs[:5]



# Version 1
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404('Question does not exist')
#     return render(request, 'polls/detail.html', {'question': question})

# Version 2
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# Version 3
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        qs = Question.objects.all()
        qs = qs.annotate(Count('choices'))
        qs = qs.filter(pub_date__lte=timezone.now())
        qs = qs.filter(choices__count__gt=0)
        return qs

# Version 1
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# Version 2
class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        qs = Question.objects.all()
        qs = qs.annotate(Count('choices'))
        qs = qs.filter(pub_date__lte=timezone.now())
        qs = qs.filter(choices__count__gt=0)
        return qs

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': "You didn't select a valid choice."
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect( reverse('polls:results', args=(question_id,) ) )
