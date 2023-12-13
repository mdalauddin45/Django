from django.shortcuts import render,redirect
from django.views import View
from .import forms
from django.contrib import messages
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
