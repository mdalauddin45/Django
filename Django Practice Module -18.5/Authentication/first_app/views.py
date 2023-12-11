from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages
# Create your views here.
def profile(request):
    return render(request, 'profile.html')
def registration(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request, "Account Created successfully")
            return redirect('register')
    else:
        form = forms.RegistrationForm()
    return render(request, 'registration.html',{ 'form': form, 'type': 'registration'})
def userlogin(request):
    return render(request, 'registration.html',{'type': 'Login'})
def userlogout(request):
    return render(request, 'registration.html')
