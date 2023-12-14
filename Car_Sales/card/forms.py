from django import forms
from .models import Card,Comment

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
        exclude = ['author']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ['name','email','body']
        