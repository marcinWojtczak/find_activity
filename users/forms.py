from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import  UserProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']


# class UserProfileUpdateForm(forms.ModelForm):

#     class Meta:
#         model = UserProfile
#         fields = ['name', 'birth_date', 'email', 'picture']