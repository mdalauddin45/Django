from typing import Any
from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Purchase

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

@login_required
def profile(request):
    user_purchases = Purchase.objects.filter(user=request.user)
    data = [purchase.car for purchase in user_purchases]
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

@login_required
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