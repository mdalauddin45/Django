from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [ 'amount', 'Transaction_type']
        
    def __init__(self, *args, **kwargs):
        self.acount = kwargs.pop('acount')
        super.__init__(self, *args, **kwargs)