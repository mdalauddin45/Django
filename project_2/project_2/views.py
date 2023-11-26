from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

# E:\Phitron\Django\project_2\templates
def Home(request):
    return HttpResponse("this is my home page")


def index(request):
    return render(request,"index.html")