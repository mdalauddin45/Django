from typing import Any
from django.shortcuts import render
from django.views import View
from .import forms
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
class registrationView(CreateView):
    template_name = 'authform.html'
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Account Created successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Creation Failed")
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']='Registration'
        return context
class UserLoginForm(LoginView):
    template_name = 'authform.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, "Account Login successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Login Failed")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

@method_decorator(login_required, name='dispatch')
class UserLogoutView(LogoutView):
    def get_success_url(self):
        messages.success(self.request, "Logout successfully")
        return reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html')