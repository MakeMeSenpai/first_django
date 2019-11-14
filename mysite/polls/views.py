# Hard way
# #grabs djangos shortcuts file and renders our views, and creates try catch shortcut
# from django.shortcuts import get_object_or_404, render
# #takes our web frame and returns a HttpResponse
# from django.http import HttpResponse
# #grabs from templates, better practice than render as render is used in hard code situations
# from django.template import loader
# #grabs our question model from all models
# from .models import Question

# # Create your views here.

# # #this is the index/home view * most simple django display
# # def index(request):
# #     return HttpResponse("Hello, world. You are at the poll index!")

# # # this is a more complex display, however it is hard coded and we want to void that
# # def index(request):
# #     #orders questions in order by date, this displays the last 5 made questions
# #     # Question does not have object attribute, this is due to pylint not understanding Django
# #     # this can be corrected by getting pylint-django
# #     latest_question_list = Question.objects.order_by('-pub_date')[:5]
# #     #joins the lists for every q(question) in questions_list (this is just a shorter in line way
# #     # to do things, and is only slightly different from what you are used to.)
# #     output = ', '.join([q.question_text for q in latest_question_list])
# #     #returns the output to our page
# #     return HttpResponse(output)

# #this display takes from templates and is much more useful
# # def index(request):
# #     latest_question_list = Question.objects.order_by('-pub_date')[:5]
# #     template = loader.get_template('polls/iindex.html')
# #     #context is our data, but iit's best practiced to call this context
# #     context = { 'latest_questioin_list': latest_question_list, }
# #     return HttpResponse(template.render(context, request))

# # However django comes with it's own shortcuts for templating, becuase of this, we will no longer 
# #need to import loader or HttpResponse when this is applied to all views
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     # params for render(request object, template name, optional third argument)
#     return render(request, 'polls/index.html', context)
# # #this is the question page view
# # def detail(request, question_id):
# #     return HttpResponse("You're looking at question %s." % question_id)

# # #after changing to djangos templating shortcut
# # def detail(request, question_id):
# #     #here we are stating a try catch, so that our errors can be displayed
# #     try:
# #         #if question can be found skip the rest
# #         question = Question.objects.get(pk=question_id)
# #     #elif question doen't exist run this
# #     except Question.DoesNotExist:
# #         #this must be included as it saves a lot of time debugging when the user can easily tell
# #         # you the error message in which you can easily find in your code later. If this is not 
# #         # included all errors would simply result in a 404 error which is unacceptable as it will
# #         # takes litteral hours just to find out what is wrong!
# #         raise Http404("Question does not exist")
# #     #only returns if try passes, this takes from template/polls.detail.html
# #     return render(request, 'polls/detail.html', {'question': question})

# # Django has a shortcut for this try catch method in which needs django.shortcuts get_objct_or_404
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# # #this is the results page view
# # def results(request, question_id):
# #     response = "You're looking at the results of question %s."
# #     return HttpResponse(response % question_id)
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# # #this is the vote page view
# # def vote(request, question_id):
# #     return HttpResponse("You're voting on question %s." % question_id)
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         #request.Post acts as a dictionary that lets you access data by key name, in this case
#         # we are returning choice'd id. These values will always be strings
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# easy way
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

#using the model attribute we tell our generic views what to expect
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) 