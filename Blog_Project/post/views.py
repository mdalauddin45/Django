from django.shortcuts import render,redirect
from .import forms
from .import models
# Create your views here.

def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            print(post_form.cleaned_data)
            post_form.save()
            return redirect('add_post')
    else:
        post_form = forms.PostForm()
    return render(request, 'post.html',{'form':post_form})

def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    print(post.title)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
            print(post_form.cleaned_data)
            post_form.save()
            return redirect('home')
    return render(request, 'post.html',{'form':post_form})