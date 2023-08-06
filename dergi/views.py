from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from Globals import *


# Create your views here.
def index(request):
    yazilar = Yazi.objects.all()
    context = {"yazilar": yazilar}
    return render(request, "index.html", context)


def yazi(request, yazi_id):
    yazi = Yazi.objects.get(pk=yazi_id)
    yazar = yazi.yazar

    context = {"yazi": yazi, "yazar": yazar}

    if request.method == "POST":
        yazi.increment()

    return render(request, "yazi.html", context)
