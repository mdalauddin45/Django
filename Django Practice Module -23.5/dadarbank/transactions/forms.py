from django import forms
from .models import Transaction
from django.contrib.auth.models import User
from accounts.models import UserBankAccount
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount',
            'transaction_type'
        ]

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account') 
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True 
        self.fields['transaction_type'].widget = forms.HiddenInput() 

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()
    
        
class DepositForm(TransactionForm):
    def clean_amount(self): 
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount') # user er fill up kora form theke amra amount field er value ke niye aslam, 50
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )

        return amount
class WithdrawForm(TransactionForm):
    def clean_amount(self):
        account = self.account
        min_withdraw_amount = 500
        max_withdraw_amount = 20000
        balance = account.balance
        amount = self.cleaned_data.get('amount')
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at least {min_withdraw_amount} $'
            )

        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at most {max_withdraw_amount} $'
            )

        if amount > balance: # amount = 5000, tar balance ache 200
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not withdraw more than your account balance'
            )

        return amount

class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        return amount

class MoneyTransferForm(forms.Form):
    recipient_account_no = forms.IntegerField(label='Recipient Account Number')
    transfer_amount = forms.DecimalField(label='Transfer Amount')

    def clean(self):
        cleaned_data = super().clean()
        recipient_account_no = cleaned_data.get("recipient_account_no")
        transfer_amount = cleaned_data.get("transfer_amount")

        # Perform validation here (e.g., recipient account exists, amount is valid, etc.)
        if recipient_account_no:
            try:
                recipient_account = UserBankAccount.objects.get(account_no=recipient_account_no)
            except UserBankAccount.DoesNotExist:
                self.add_error('recipient_account_no', 'Recipient account does not exist.')
        
        # Additional validation logic if needed
        if transfer_amount and transfer_amount <= 0:
            self.add_error('transfer_amount', 'Transfer amount must be greater than zero.')

        return cleaned_data