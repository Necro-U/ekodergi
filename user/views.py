from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def sign_up(request):
    print(request.method)
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        print(form.error_messages)
        if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form = RegistrationForm()

    return render(request, "registration/sign_up.html", {"form": form})
