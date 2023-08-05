from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Yazi)
class InfoAdmin(admin.ModelAdmin):
    list_display = ["isim"]
    search_fields = ["isim"]

    class Meta:
        Yazi
