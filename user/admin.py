from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Yazar
from django.forms import Textarea

# Register your models here.


class YazarAdminConfig(UserAdmin):
    model = Yazar
    search_fields = ("email", "username", "first_name")
    list_filter = ("email", "username", "first_name", "is_active", "is_staff")
    ordering = ("-start_date",)
    list_display = (
        "email",
        "username",
        "first_name",
        "is_active",
        "is_staff",
    )

    fieldsets = (
        (None, {"fields": ("email", "username", "password", "first_name", "category")}),
        ("Permissions", {"fields": ("is_active", "is_staff")}),
        ("Personal", {"fields": ("about",)}),
    )

    formfield_overrides = {
        Yazar.description: {"widget": Textarea(attrs={"rows": 10, "cols": 40})},
    }


admin.site.register(Yazar, YazarAdminConfig)
