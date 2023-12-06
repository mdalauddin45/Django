from django import forms
from .models import Album

class AlbulForm(forms.Form):
    class Meta:
        model = Album
        fields = '__all__'