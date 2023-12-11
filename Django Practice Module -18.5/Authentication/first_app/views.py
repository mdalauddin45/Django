from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile(request):
    return render(request, 'profile.html')

def registration(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request, "Account Created successfully")
            return redirect('login')
    else:
        form = forms.RegistrationForm()
    return render(request, 'registration.html',{ 'form': form, 'type': 'Registration'})

def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username=name, password=userpass)
            if user is not None:
                login(request,user)
                messages.success(request,"login successfully")
                return redirect('profile')
            else:
                messages.warning(request,"Login Failed")
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, 'registration.html',{'form':form, 'type': 'Login'})

def userlogout(request):
    logout(request)
    messages.success(request,"logout successfully")
    return redirect('login')

def charngepassword(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Password Changes Succesfully")
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'registration.html',{'form':form, 'type': 'Change password'})