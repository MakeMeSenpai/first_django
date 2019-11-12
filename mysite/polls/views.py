#grabs djangos shortcuts file and renders our views
from django.shortcuts import render
#takes our web frame and returns a HttpResponse
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You are at the poll index!")