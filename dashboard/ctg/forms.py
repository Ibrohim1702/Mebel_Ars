from django import forms

from sayt.models import User


class CtgForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

