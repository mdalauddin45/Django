from typing import Any
from django import forms
from django.core import validators
# widgets == field to html input 

def len_check(value):
    if len(value) <10:
        return forms.ValidationError("Enter a value less than 10 characters")

class contactForm(forms.Form):
    # name = forms.CharField(label="Full Name: ", initial="alauddin", help_text="Total length must be within 70 characters", required=False, widget=forms.Textarea(attrs={'id': 'text_area','class':'class1 class2','placeholder':'Enter Your name'}))
    name = forms.CharField(label="Full Name: ", widget=forms.TextInput, validators=[validators.MaxLengthValidator(10, message='Enter a name with at least 10 characters')])
    text = forms.CharField(widget=forms.TextInput,validators=[len_check])
    email = forms.CharField(label="Email address",widget=forms.EmailInput,validators=[validators.EmailValidator(message='Enter a valid email address')])
    age = forms.IntegerField(label="Age", validators=[validators.MaxValueValidator(34, message="age must be maximum 34"), validators.MinValueValidator(18,message="age must be minimum 18")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'],message='File extension must begin with pdf or png')])
    # weight = forms.FloatField(label="Weight")
    # balance = forms.DecimalField(label="Balance")
    # checked = forms.BooleanField(label="Check")
    # birthday = forms.DateField(label="Birthday",widget=forms.DateInput(attrs={'type': 'date'}))
    # appointment = forms.DateTimeField(label="Appointment",widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    # CHOICES = [('S', 'smail'),('M', 'Medium'),('L', 'large')]
    # ratting = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    # meal = [('P', 'Pepperoni'),('M', 'Masrum'),('B', 'Beef')]
    # pizza = forms.MultipleChoiceField(choices=meal, label="Pizza",widget=forms.CheckboxSelectMultiple)
    
class passwordValidationFrom(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        con_pass = self.cleaned_data['confirm_password']
        user_name = self.cleaned_data['name']
        if val_pass != con_pass:
            raise forms.ValidationError('password does not match')
        if len(user_name) <15:
            raise forms.ValidationError('Name must be at least 15 characters')
