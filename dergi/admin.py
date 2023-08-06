from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Yazi)
class InfoAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]

    class Meta:
        Yazi


@admin.register(Yazar)
class InfoAdmin(admin.ModelAdmin):
    list_display = ["isim"]
    search_fields = ["isim", "soyisim"]

    class Meta:
        Yazar


@admin.register(Konu)
class InfoAdmin(admin.ModelAdmin):
    list_display = ["konu_isim"]
    search_fields = ["konu_isim"]

    class Meta:
        Konu
