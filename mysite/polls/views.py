#grabs djangos shortcuts file and renders our views
from django.shortcuts import render
#takes our web frame and returns a HttpResponse
from django.http import HttpResponse
#grabs our question model from all models
from .models import Question

# Create your views here.

# #this is the index/home view
# def index(request):
#     return HttpResponse("Hello, world. You are at the poll index!")
def index(request):
    #orders questions in order by date, this displays the last 5 made questions
    # Question does not have object attribute.... don't know why
    latest_question_list = Question.object.order_by('-pub_date')[:5]
    #joins the lists for every q(question) in questions_list (this is just a shorter in line way
    # to do things, and is only slightly different from what you are used to.)
    output = ', '.join([q.question_text for q in latest_question_list])
    #returns the output to our page
    return HttpResponse(output)

#this is the question page view
def detail(request, question_id):
    return HttpResponse("You're looking at question%s." % question_id)

#this is the results page view
def results(request, question_id):
    response = "You're looking at the results of question%s."
    return HttpResponse(response % question_id)

#this is the vote page view
def vote(request, question_id):
    return HttpResponse("You're voting on question%s." % question_id)