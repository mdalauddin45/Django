from django.shortcuts import render

# Create your views here.
def musician(request):
    return render(request, 'musician.html')