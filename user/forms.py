from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Yazar, Yazi


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Yazar
        fields: list[str] = ["username", "email", "category", "password1", "password2"]


class NewYazi(forms.ModelForm):
    class Meta:
        model = Yazi
        fields: list[str] = ["title", "content"]
