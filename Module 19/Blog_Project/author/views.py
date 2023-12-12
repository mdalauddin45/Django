from typing import Any
from django.shortcuts import render,redirect
from .import forms
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post.models import Post
from django.contrib.auth.views import LoginView,LogoutView

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
                return redirect('profile')
            else:
                messages.warning(request, "Login failed")
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request,'registerform.html',{'form':form, 'type': 'Login'})

class UserLoginView(LoginView):
    template_name = 'registerform.html'
    success_url = reverse_lazy('profile')
    #if success_url is not working
    # def get_success_url(self):
    #     return reverse_lazy('profile')
    
    def form_valid(self,form):
        messages.success(self.request,"login successfully")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.warning(self.request,"Login failed")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']= 'Login'
        return context

def userLogout(request):
    logout(request)
    return redirect('login')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')

@login_required
def profile(request):
    data = Post.objects.filter(author= request.user)
    return render(request, 'profile.html',{'data':data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            print(profile_form.cleaned_data)
            profile_form.save()
            messages.success(request, "Profile Updated successfully")
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserForm(instance=request.user)
    return render(request, 'update_profile.html',{'form':profile_form, 'type': 'Profile'})

def passcharnge(request):
    if request.method == 'POST':
        form =PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request, "Paswrod Changes successfully")
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'passchange.html',{'form':form, 'type': 'Password Form'})
        
