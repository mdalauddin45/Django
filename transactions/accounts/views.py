from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm, MoneyTransferForm
from django.urls import reverse_lazy
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.views import View
from .models import UserBankAccount

# Create your views here.
class UserRegistrationView(FormView):
    template_name = 'registerform.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'registerform.html'
    def ger_success_url(self):
        return reverse_lazy('home')
    
class UserLogoutView(LogoutView):
    def ger_success_url(self):
        if self.request.user.is_authenticated():
            logout(self.request)
        return reverse_lazy('home')
class UserBankAccountUpdateView(View):
    template_name = 'profile.html'
    
    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name,{'form':form})
    
    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form':form})

class MoneyTransferView(FormView):
    template_name = 'transfer_form.html'
    form_class = MoneyTransferForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        sender_account = UserBankAccount.objects.get(user=self.request.user)  # Assuming sender is the logged-in user
        recipient_account_no = form.cleaned_data['recipient_account_no']
        transfer_amount = form.cleaned_data['transfer_amount']

        recipient_account = UserBankAccount.objects.filter(account_no=recipient_account_no).first()

        if not recipient_account:
            form.add_error('recipient_account_no', 'Recipient account does not exist.')
            return self.form_invalid(form)

        # Perform the money transfer
        sender_account.money_transfer(recipient_account, transfer_amount)
        return super().form_valid(form)