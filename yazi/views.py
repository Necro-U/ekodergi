from django.shortcuts import render
from .models import *

# Create your views here.


def yazi_ozel(request, id):
    yazi = Yazi.objects.get(id=id)
    return render(request, "yazi.html", {"yazi": yazi})
