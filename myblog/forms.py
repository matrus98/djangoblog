from django import forms
from .models import Post

class ImgForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image']

class PostForm(forms.ModelForm):

    title = forms.CharField(help_text='max 200 characters')
    class Meta:
        model = Post
        fields = ['title', 'text', 'image']