from django.shortcuts import render
from .import forms
# Create your views here.

def add_author(request):
    author_form = forms.AuthorForm()
    return render(request, 'author.html',{'form':author_form})