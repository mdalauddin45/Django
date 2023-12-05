from django.shortcuts import render,redirect
from .import forms
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