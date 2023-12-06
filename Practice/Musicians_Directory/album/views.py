from django.shortcuts import render,redirect
from .import forms

# Create your views here.
def album(request):
    if request.method =="POST":
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('album')
    else:
        form = forms.AlbumForm()
    return render(request, 'album.html',{'form':form})