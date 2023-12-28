from django.shortcuts import render, redirect
from .forms import UserRegistrationForm,UserUpdateForm
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.contrib import messages
from django.contrib.auth import login, logout,update_session_auth_hash
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_transaction_email(user,amount,subject,template):
    message = render_to_string(template,{
        'user': user,
        'amount':amount,
    })
    send_email = EmailMultiAlternatives(subject, '',to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()

class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form)
    

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')


class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})

# class PasswordChangeView(View):
#     def post(self, request):
#         form = SetPasswordForm(request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Password changed successfully")
#             update_session_auth_hash(request, form.user)
#             return redirect('profile')
#         return render(request, 'accounts/passchange.html', {'form': form, 'type': 'Password Form'})
    
#     def get(self, request):
#         form = SetPasswordForm(user=request.user)
#         return render(request, 'accounts/passchange.html', {'form': form, 'type': 'Password Form'})
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
    return render(request, 'accounts/passchange.html',{'form':form, 'type': 'Change password'})