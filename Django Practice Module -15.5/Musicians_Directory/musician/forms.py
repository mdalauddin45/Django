from django import forms
from .models import Musician

class AlbulForm(forms.Form):
    class Meta:
        model = Musician
        fields = '__all__'