from django import forms

from sayt.models import Employees


class CtgForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"

