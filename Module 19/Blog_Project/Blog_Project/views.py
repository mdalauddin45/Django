from django.shortcuts import render
from post.models import Post
from categories.models import Category
# Create your views here.

def home(request,category_slug=None):
    data = Post.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug=category_slug)
        data = Post.objects.filter(category=category)
    categories = Category.objects.all()
    response = render(request, 'home.html',{'data':data, 'category':categories})
    response.set_cookie('name',' alauddin')
    return response

def get_cookies(request):
    name = request.COOKIES.get('name')
    return render(request, 'get_cookies.html',{'name':name})

def del_cookies(request):
    response = render(request,'del_cookies.html')
    response.delete_cookie('name')
    return response