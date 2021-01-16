from django.forms import ModelForm
from .models import Post
from django import forms
# from .models import


class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'city']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
        }

        # 'user': forms.Select(attrs={'class': 'form-control'}),
