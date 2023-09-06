from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Yazi)
class InfoAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "yazar", "created_date", "image"]
    list_display_links = ["title", "yazar"]
    search_fields = ["title"]
    list_filter = ["created_date"]

    class Meta:
        model = Yazi
