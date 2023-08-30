from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Yazar, Yazi


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Yazar
        fields: list[str] = ["username", "email", "category", "password1", "password2"]


class NewYazi(forms.ModelForm):
    # title = forms.CharField(max_length=200, label="Başlık")
    # content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Yazi
        fields: list[str] = ["title", "content"]

    # image = forms.ImageField(required=False)

    # def save(self):
    #     t = self.cleaned_data["title"]
    #     c = self.cleaned_data["content"]
    #     # t = self.cleaned_data["title"]
    #     new_yazi = Yazi()
