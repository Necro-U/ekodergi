from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Yazar


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Yazar
        fields = ["username", "email", "category", "password1", "password2"]
