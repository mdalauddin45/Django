from django.shortcuts import render
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')
def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Created Successfully')
            form.save()
            print(form.cleaned_data)
    else:
        form = RegisterForm()
    return render(request,'signup.html',{'form':form})