from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Yazar
from django.forms import Textarea

# Register your models here.


class YazarAdminConfig(UserAdmin):
    model = Yazar
    search_fields = ("username", "email", "first_name")
    list_filter = ("username", "email", "first_name", "is_active", "is_staff")
    ordering = ("-start_date",)
    list_display = (
        "username",
        "email",
        "first_name",
        "is_active",
        "is_staff",
    )

    fieldsets = (
        (None, {"fields": ("username", "email", "password", "first_name", "category")}),
        ("Permissions", {"fields": ("is_active", "is_staff")}),
        ("Personal", {"fields": ("description",)}),
    )

    formfield_overrides = {
        Yazar.description: {"widget": Textarea(attrs={"rows": 10, "cols": 40})},
    }
    add_fieldsets = [
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "category",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        )
    ]


admin.site.register(Yazar, YazarAdminConfig)
