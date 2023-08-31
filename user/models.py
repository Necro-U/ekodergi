from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy
from django.utils import timezone


class YazarManager(BaseUserManager):
    def create_user(self, email, username, first_name, password, category, **others):
        if not email:
            raise ValueError(gettext_lazy("You must provide an email "))

        self.normalize_email(email)
        user = self.model(
            email=email, username=username, first_name=first_name, category=category
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, password, **others):
        others.setdefault("is_staff", True)
        others.setdefault("is_superuser", True)
        others.setdefault("is_active", True)

        if not others.get("is_staff"):
            raise ValueError("Superuser must be assigned to is_staff = True")

        if not others.get("is_superuser"):
            raise ValueError("Superuser must be assigned to is_superuser = True")

        return self.create_user(email, username, first_name, password, **others)


class Yazar(AbstractUser, PermissionsMixin):
    CATEGORIES = {
        ("teknoloji", "teknoloji"),
        ("ekonomi", "ekonomi"),
        ("mutfak", "mutfak"),
        ("hikaye", "hikaye"),
    }
    email = models.EmailField(unique=True)
    category = models.CharField(max_length=100, choices=CATEGORIES, default="teknoloji")
    description = models.TextField(
        "Description", max_length=300, default="", blank=True
    )
    start_date = models.DateTimeField(default=timezone.now())

    objects = YazarManager()

    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email", "category", "first_name"]

    def __str__(self) -> str:
        return self.username


class Yazi(models.Model):
    yazar = models.ForeignKey("Yazar", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="", name="title")
    content = models.TextField(max_length=2000, default="", name="content")
    created_date = models.DateTimeField(default=timezone.now())

    # image = models.ImageField(upload_to=f"yazilar/")
    def __str__(self) -> str:
        return self.title
