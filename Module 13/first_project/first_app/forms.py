from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="username")
    email = forms.EmailField(label="Email address")