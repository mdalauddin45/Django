from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [ 'amount', 'Transaction_type']
        
    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('acount')
        super.__init__(self, *args, **kwargs)
        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput()
        
    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction= self.account.balance
        return super().save()

class DepositForm(Transaction):
    def clean_amount(self):
        min_deposit_amount = 100
        amount = self.clean_data.get('amount')
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at last {min_deposit_amount} $'
            )
        return amount

#transactionform ta sob kany inherit kory kaj kora holo
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

        if amount > balance: 
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not withdraw more than your account balance'
            )

        return amount



class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        return amount