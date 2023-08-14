from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from Globals import *


# Create your views here.
def index(request):
    konular = Konu.objects.all()
    context = {"konular": konular}
    return render(request, "index.html", context)


def yazi(request, yazi_id):
    yazi = Yazi.objects.get(pk=yazi_id)
    yazar = yazi.yazar
    context = {"yazi": yazi, "yazar": yazar}

    if request.method == "POST" and request.POST["like"]:
        yazi.increment()

    return render(request, "yazi.html", context)


def konu(request, konu_id):
    konu = Konu.objects.get(pk=konu_id)
    yazarlar = konu.yazar_set.all()
    context = {"konu": konu, "yazarlar": yazarlar}

    return render(request, "konu.html", context)


def login(request):
    if not request.user.is_authenticated:
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,
            password=password
            )
            if user is not None :
                auth_login(request, user)
                return redirect("home")
            else:
                messages.error(
                    request,"Kullanıcı adı veya şifre hatalı."
                    )
    else:
        return render (
            request,
            'login.html', {'form':""})
            


def new_yazi(request):
    icerik = str()
