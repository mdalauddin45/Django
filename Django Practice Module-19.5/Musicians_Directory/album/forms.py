from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name', 'musicians', 'album_release_date', 'ratting']
        widgets = {
            'album_release_date': forms.DateInput(attrs={'type': 'date'}),
        }