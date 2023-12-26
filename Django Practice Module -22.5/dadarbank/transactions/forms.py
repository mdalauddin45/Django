from django import forms
from .models import Transaction , MoneyTransaction
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
    
class MoneyTransactionForm(forms.ModelForm):
    class Meta:
        model = MoneyTransaction
        fields = [
            'account_no',
            'amount',
        ]

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        # Your validation logic for the transaction amount can be added here
        # For example, ensuring the amount is positive, etc.
        return amount

    def save(self, commit=True):
        # This is assuming you have an 'account' attribute passed to the form
        account = self.account
        instance = super().save(commit=False)
        instance.balance_after_transaction = account.balance + instance.amount
        instance.save()
        return instance


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
        