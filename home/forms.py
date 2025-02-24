from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'website', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
        }
