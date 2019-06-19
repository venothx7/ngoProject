from django import forms
from .models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['first_name', 'last_name', 'email', 'address', 'adult_qty', 'child_qty']
