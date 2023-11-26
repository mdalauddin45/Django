from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse("this is first_app courses page")
def about(request):
    return HttpResponse("this is first_app About page")
def Home(request):
    return HttpResponse("this is first_app Home page")
