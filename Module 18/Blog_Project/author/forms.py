from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = '__all__'
        # field = ['name','bio']

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']