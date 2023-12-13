from typing import Any
from django.shortcuts import render,redirect
from django.views import View
from .import forms
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.
class registrationView(View):
    def get(self,request):
        form = forms.RegistrationForm()
        return render(request,'authform.html',{'form': form, 'type': 'Registration'})
    
    def post(self,request):
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created successfully")
            return redirect('login')
        return render(request,'authform.html',{'form': form, 'type': 'Registration'})

class UserLoginForm(LoginView):
    template_name = 'authform.html'
    success_url= reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(form, "Account Login successfully")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(form, "Login Failed")
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']='Login'
        return context
    
