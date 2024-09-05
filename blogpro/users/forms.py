from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import ProfileModel, OTPModel

class SignupForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta():
        model=User
        fields=('username', 'email' )
    def __init__(self, *args, **kwargs ) :
        super(SignupForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email']:
            self.fields[fieldname].help_text=None

class LoginForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta():
        model=User
        fields=['email']
        

class UserUpdateForm(forms.ModelForm):
    class Meta():
        model=User
        fields=['username', 'email']
    def __init__(self, *args, **kwargs ) :
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','email']:
            self.fields[fieldname].help_text=None

class ProfileUpdateForm(forms.ModelForm):
    class Meta():
        model=ProfileModel
        fields=['image']

class OTPForm(forms.ModelForm):
    class Meta():
        model=OTPModel
        fields=['otp']
