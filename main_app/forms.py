from django import forms
from .models import Post

class ImageForm(forms.ModelForm):
    """Form for the post model"""
    class Meta:
        model = Post
        fields = '__all__'