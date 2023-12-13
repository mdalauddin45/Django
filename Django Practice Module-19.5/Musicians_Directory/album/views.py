from django.shortcuts import render,redirect
from .import forms
from .import models


# Create your views here.
def album(request):
    if request.method =="POST":
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = forms.AlbumForm()
    return render(request, 'album.html',{'form':form})

def edit_album(request,id):
    album = models.Album.objects.get(pk=id)
    form = forms.AlbumForm(instance=album)
    if request.method == "POST":
        form = forms.AlbumForm(request.POST, instance=album)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
    return render(request, 'album.html',{'form':form})

def delete_album(request,id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return redirect('home')