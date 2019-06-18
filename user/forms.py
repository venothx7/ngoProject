from django import forms
from .models import User
from bootstrap_modal_forms.forms import BSModalForm


class UserForm(BSModalForm):
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'email',
                  'password',
                  'role',]
