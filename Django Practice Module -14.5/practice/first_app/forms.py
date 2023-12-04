from typing import Any
from django import forms 
import datetime

class ContactForm(forms.Form):
    title = forms.CharField() 
    description = forms.CharField()  
    first_name = forms.CharField(max_length = 200, initial="Ala")  
    last_name = forms.CharField(max_length = 200, initial="Uddin")  
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")  
    password = forms.CharField(widget = forms.PasswordInput()) 
    comment = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    message = forms.CharField(max_length = 10,help_text="Enter only 10 characters")   
    day = forms.DateField(initial=datetime.date.today)
    Favorite_color_choices =[('blue','Blue'),('green','Green'),('yellow','yellow')]
    favorite_color = forms.ChoiceField(choices=Favorite_color_choices)
    favorite_colors = forms.MultipleChoiceField(choices=Favorite_color_choices,widget=forms.CheckboxSelectMultiple)

    