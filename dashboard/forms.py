from django import forms

from account.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['password', 'data_joined', 'email']