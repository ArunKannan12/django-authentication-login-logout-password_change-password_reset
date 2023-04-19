from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.views import PasswordResetView

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter user name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter E-mail'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-enter password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'your class',
        'placeholder': ' Enter your email address',
        'type': 'email',
        'name': 'email',
        'style':'width:500px;height:50px;border-radius:10px;border:2px skyblue solid;'
        }))

class UserSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserSetPasswordForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password',
        'name': 'password1',
        'autocomplete':'new-password',
        'style':'width:500px;height:50px;border-radius:10px;border:2px skyblue solid;'
        
    }))
    new_password2 = forms.CharField(label='Conform Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Re-enter new Password',
        'type': 'password',
        'name': 'password2',
        'autocomplete':'new-password',
        'style':'width:500px;height:50px;border-radius:10px;border:2px skyblue solid;'
        
    }))