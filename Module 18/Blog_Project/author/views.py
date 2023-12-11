from django.shortcuts import render,redirect
from .import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

# def add_author(request):
#     if request.method == 'POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             print(author_form.cleaned_data)
#             author_form.save()
#             return redirect('add_author')
#     else:
#         author_form = forms.AuthorForm()
#     return render(request, 'author.html',{'form':author_form})

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            print(register_form.cleaned_data)
            register_form.save()
            messages.success(request, "Account Created successfully")
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'registerform.html',{'form':register_form, 'type': 'Registration'})

def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username= name, password= userpass)
            if user is not None:
                login(request, user)
                messages.success(request,"login successfully")
                return redirect('login')
            else:
                messages.warning(request, "Login failed")
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request,'registerform.html',{'form':form, 'type': 'Login'})

def userLogout(request):
    logout(request)
    return redirect('login')
        
            
            