from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'home.html',{'form':form})
    else:
        form = ContactForm()
        return render(request, 'home.html',{'form':form})