from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="username")
    email = forms.EmailField(label="Email address")
    age = forms.IntegerField(label="Age")
    weight = forms.FloatField(label="Weight")
    balance = forms.DecimalField(label="Balance")
    checked = forms.BooleanField(label="Check")
    birthday = forms.DateField(label="Birthday")
    appointment = forms.DateTimeField(label="Appointment")