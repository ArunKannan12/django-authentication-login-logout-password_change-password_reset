from .models import *
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter user name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter E-mail'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-enter password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("An user with this email already exists!")
        return email

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
class changepassword(PasswordChangeForm): 
    def __init__(self, *args, **kwargs):
        super(changepassword, self).__init__(*args, **kwargs)
    error_messages={
        **SetPasswordForm.error_messages,
        'password_incorrect': ("your old password was entered incorrectly. Please enter it again "),
    }
    old_password=forms.CharField(label=("old password"),strip=False,widget=forms.PasswordInput(attrs={'class': 'form-control',
        'placeholder': 'Enter your old Password',
        'type': 'password',
        'name': 'old_password',
        'autocomplete':'current-password',
        'style':'width:500px;height:50px;border-radius:10px;border:2px skyblue solid;',
        'autofocus':True}))
    new_password1=forms.CharField(label=("new password1"),strip=False,widget=forms.PasswordInput(attrs={'class': 'form-control',
        'placeholder': 'Enter your new Password',
        'type': 'password',
        'name': 'new_password1',
        'autocomplete':'current-password',
        'style':'width:500px;height:50px;border-radius:10px;border:2px skyblue solid;',
        'autofocus':True}))
    new_password2=forms.CharField(label=("new password2"),strip=False,widget=forms.PasswordInput(attrs={'class': 'form-control',
        'placeholder': 'Re-enter your new Password',
        'type': 'password',
        'name': 'new_password2',
        'autocomplete':'current-password',
        'style':'width:500px;height:50px;border-radius:10px;border:2px skyblue solid;',
        'autofocus':True}))
    def clean_old_password(self):
        old_password=self.cleaned_data['old_password']
        if not self.user.check_password(old_password):
            raise ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password