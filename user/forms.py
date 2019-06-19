# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from bootstrap_modal_forms.forms import BSModalForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'password',
            'role',
            'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'password',
            'role',
            'email')
        
class SignupForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name', 
            'last_name', 
            'email', 
            'password', 
            ]

class UserForm(BSModalForm):
    class Meta:
        model = CustomUser
        fields = ['first_name',
                  'last_name',
                  'email',
                  'password',
                  'role',]
