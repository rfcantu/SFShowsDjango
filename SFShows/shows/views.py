from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Creating a view called index
def index(request):
    return HttpResponse("Hello world, you are looking for shows.")