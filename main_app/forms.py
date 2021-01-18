from django.forms import ModelForm
from .models import Post, City
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
# from .models import


class SignUpForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'city']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
        }


class City_Form(ModelForm):
    class Meta:
        model = City
        fields = ['name', 'description', 'flags']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'flag': forms.TextInput(attrs={'class': 'form-control'}),
        }
