from django import forms
from Landing import models


class RegisterUser(forms.ModelForm):
    class Meta:
        model = models.User
        exclude = [""]