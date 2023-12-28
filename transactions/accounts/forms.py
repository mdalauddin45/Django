from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserBankAccount, UserAddress
from django.contrib.auth.models import User 
from .constants import ACCOUNT_TYPE, GENDER_TYPE

class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'account_type', 'birth_date','gender', 'postal_code', 'city','country', 'street_address']
    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit==True:
            our_user.save()
            account_type = self.cleaned_data.get('account_type')
            gender = self.cleaned_data.get('gender')
            postal_code = self.cleaned_data.get('postal_code')
            country = self.cleaned_data.get('country')
            birth_date = self.cleaned_data.get('birth_date')
            city = self.cleaned_data.get('city')
            street_address = self.cleaned_data.get('street_address')
        UserAddress.objects.create(
                user = our_user,
                postal_code = postal_code,
                country = country,
                city = city,
                street_address = street_address
            )
        UserBankAccount.objects.create(
                user = our_user,
                account_type  = account_type,
                gender = gender,
                birth_date =birth_date,
                account_no = 100+ our_user.id
            )
        return our_user
class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            user_account, created = UserBankAccount.objects.get_or_create(user=user) # jodi account thake taile seta jabe user_account ar jodi account na thake taile create hobe ar seta created er moddhe jabe
            user_address, created = UserAddress.objects.get_or_create(user=user) 

            user_account.account_type = self.cleaned_data['account_type']
            user_account.gender = self.cleaned_data['gender']
            user_account.birth_date = self.cleaned_data['birth_date']
            user_account.save()

            user_address.street_address = self.cleaned_data['street_address']
            user_address.city = self.cleaned_data['city']
            user_address.postal_code = self.cleaned_data['postal_code']
            user_address.country = self.cleaned_data['country']
            user_address.save()

        return user

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