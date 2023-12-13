from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name', 'musician', 'album_release_date', 'rating']
        widgets = {
            'album_release_date': forms.DateInput(attrs={'type': 'date'}),
        }