from django.shortcuts import render
from category.models import Category
# Create your views here.
def home(request,category_slug=None):
    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)
    categories = Category.objects.all()
    return render(request,'home.html',{'categories':categories})