from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User
from django import forms
from .constants import ACCOUNT_TYPE,GENDER_TYPE
from .models import UserBankAccount, UserAdderss

class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.CharField(max_length=10, choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ['username','password1','password2','first_name','last_name','email','city','street_address','account_type','birth_date' ,'gender','postal_code','country']
    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            account_type = self.cleaned_data.get('account_type')
            gender = self.cleaned_data.get('gender')
            postal_code = self.cleaned_data.get('postal_code')
            country = self.cleaned_data.get('country')
            birth_date = self.cleaned_data.get('birth_date')
            city = self.cleaned_data.get('city')
            street_address = self.cleaned_data.get('street_address')
            
            UserAdderss.objects.create(
                user = our_user,
                postal_code=postal_code,
                city=city,
                street_address=street_address,
            )
            UserBankAccount.objects.create(
                user = our_user,
                account_type=account_type,
                gender= gender,
                birth_date=birth_date,
                account_no=1212000600+our_user.id
            )
        return our_user