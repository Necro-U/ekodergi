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
    begeni = yazi.begeni_set.all()
    context = {"yazi": yazi, "begeni": begeni}
    return render(request, "yazi.html", context)
