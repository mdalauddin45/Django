from django.shortcuts import render
from post.models import Post
# Create your views here.

def home(request):
    data = Post.objects.all
    return render(request, 'home.html',{'data':data})