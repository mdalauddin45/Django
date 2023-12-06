from django.shortcuts import render,redirect
from .import forms
from .import models

# Create your views here.
def musician(request):
    if request.method =="POST":
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('musician')
    else:
        form = forms.MusicianForm()
    return render(request, 'musician.html',{'form':form})