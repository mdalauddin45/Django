from django.shortcuts import render

# Create your views here.
def add_category(request):
    return render(request, 'category.html')