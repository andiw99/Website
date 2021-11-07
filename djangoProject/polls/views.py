from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import QuestionForm, ChoiceForm
from django.forms import formset_factory

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    print("latest question list", latest_question_list)
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def createview(request, nr_of_choices):
    # initialize forms
    nr_of_choices = max(nr_of_choices, 1)
    form = QuestionForm(request.POST or None)
    choiceFormSet = formset_factory(ChoiceForm, extra=nr_of_choices)
    choice_forms = choiceFormSet(request.POST or None)
    single_choice_form = ChoiceForm(request.POST or None)

    # save question to get question id
    if form.is_valid():
        form.save()

    valid_choices = 0
    for choice_form in choice_forms:
        if choice_form.is_valid():
            # create choice instance
            print("laufen wir hier rein?")
            try:
                valid_choices += 1
                c = Choice( question=Question.objects.last(),
                            choice_text=choice_form.cleaned_data["choice_text"],
                            votes=choice_form.cleaned_data["votes"]
                            )
                c.save()
            except KeyError:
                pass


    if not valid_choices and form.is_valid():
        Question.objects.last().delete()
    else:
        form = QuestionForm()
    choice_forms = choiceFormSet()
    context = {
        "form": form,
        "choice_forms": choice_forms,
        "nr_of_choices": nr_of_choices,
    }

    return render(request, "polls/create.html", context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        excludes any questions that aren't published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"