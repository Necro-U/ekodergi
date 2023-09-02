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
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main")
    else:
        form = RegistrationForm()

    return render(request, "registration/sign_up.html", {"form": form})


@login_required(login_url="/user/login")
def profile(request):
    return render(request, "user/profile.html", {})


@login_required(login_url="/user/login")
def create_yazi(request):
    print(request.method)

    if request.method == "POST":
        form = NewYazi(request.POST)
        print(form.errors)
        if form.is_valid():
            infos = form.save(commit=False)
            infos.yazar = request.user
            infos.save()
            print(infos.yazar)
            return render(
                request, "/user/yazi_galeri.html"
            )  # Bu yazi galeri profilin yazılarının bulundupu bölüm
    else:
        form = NewYazi()
    return render(request, "yazilar/yazi_ekle.html", {"form": form})


login_required(login_url="/user/login")


def show_yazis(request):
    user = Yazar.objects.get(username=request.user)
    yazis = user.yazi_set.all()
    return render(request, "yazilar/yazi_galeri.html", {"yazis": yazis})


def show_yazi(request, id):
    yazi = Yazi.objects.get(id=id)
    context = {"yazi": yazi}
    return render(request, f"yazilar/yazi.html", context)


def add_category(request):
    if request.method == "POST":
        form = NewCategory(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "yazilar/yazi_galeri.html", {})

    form = NewCategory()

    return render(request, "kategori.html", {"form": form})
