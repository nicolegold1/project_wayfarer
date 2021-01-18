from django.forms import ModelForm
# from .models import

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from accounts.models import UserProfile


class EditProfileForm(ModelForm)
    class Meta:
        model = User
        fields = ['username','password', 'cities', 'profile image']

class ProfileForm(ModelForm):
         class Meta:
         model = User
         fields = ['username','password','cities']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('cities', 'country') #Note that we didn't mention user field here.

    def save(self, user=None):
        user_profile = super(UserProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile