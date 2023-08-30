from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def sign_up(request):
    # print(request.method)
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        # print(form.error_messages)
        # print(form.is_valid())
        # print(form.data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main")
    else:
        form = RegistrationForm()

    return render(request, "registration/sign_up.html", {"form": form})


@login_required(login_url="user:login")
def profile(request):
    return render(request, "user/profile.html", {})


@login_required(login_url="user:login")
def create_yazi(request):
    print(request.method)

    if request.method == "POST":
        # yazar = request.POST.get("yazar", "")
        # baslik = request.POST.get("title", "")
        # icerik = request.POST.get("icerik", "")
        # image = request.POST.get("image", "")
        form = NewYazi(request.POST)
        print(form.errors)
        if form.is_valid():
            infos = form.save(commit=False)
            infos.yazar = request.user
            infos.save()
            print(infos.yazar)
            return render(
                request, f"yazi_galeri/0"
            )  # Bu yazi galeri profilin yazılarının bulundupu bölüm
    else:
        form = NewYazi()
    return render(request, "yazilar/yazi_ekle.html", {"form": form})


login_required(login_url="user:login")


def show_yazis(request):
    user = Yazar.objects.get(username=request.user)
    yazis = user.yazi_set.all()
    return render(request, "yazilar/yazi_galeri.html", {"yazis": yazis})
