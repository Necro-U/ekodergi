from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy
from django.utils import timezone
from website.settings import *
from website.settings import *


class Kategori(models.Model):
    name = models.CharField(max_length=100, name="name", unique=True)

    def __str__(self) -> str:
        return self.name


class YazarManager(BaseUserManager):
    def create_user(self, email, username, first_name, password, **others):
        if not email:
            raise ValueError(gettext_lazy("You must provide an email "))

        # obj = Kategori.objects.create(isim="Ma")

        self.normalize_email(email)
        user = self.model(
            email=email, username=username, first_name=first_name, **others
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
    email = models.EmailField(unique=True)
    category = models.ForeignKey(
        "Kategori", on_delete=models.CASCADE, blank=True, null=True
    )
    description = models.TextField(
        "Description", max_length=300, default="", blank=True
    )
    start_date = models.DateTimeField(default=timezone.now())
    height = models.PositiveIntegerField(default=360)
    width = models.PositiveIntegerField(default=360)
    image = models.ImageField(
        default="default_user_image.jpg",
        upload_to="users/",
        height_field="height",
        width_field="width",
    )
    objects = YazarManager()

    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email", "first_name"]

    def __str__(self) -> str:
        return self.username


class Yazi(models.Model):
    yazar = models.ForeignKey("Yazar", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="", name="title")
    content = models.TextField(max_length=2000, default="", name="content")
    created_date = models.DateTimeField(default=timezone.now())
    image = models.ImageField(
        upload_to="images/",
        default="default_user_image.jpg",
    )

    def __str__(self) -> str:
        return self.title
