from typing import Any
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.utils import timezone

# Create your models here.


class Konu(models.Model):
    konu_isim = models.CharField("Konu", max_length=50)

    def __str__(self) -> str:
        return self.konu_isim


class Yazar(AbstractBaseUser):
    username = models.CharField("Kullanıcı adı", max_length=50, unique=True)
    isim = models.CharField("İsim", max_length=100)
    soyisim = models.CharField("Soyisim", max_length=50)
    image = models.ImageField("Fotoğraf")
    konu = models.ForeignKey(Konu, on_delete=models.CASCADE)
    # sifre = models.CharField("Şifre", max_length=100)
    email = models.EmailField("Email", unique=True)
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["isim", "soyisim", "konu", "sifre", "email"]

    def __str__(self) -> str:
        return self.isim


class Yazi(models.Model):
    title = models.CharField("Yazı Başlığı", max_length=100)
    icerik = models.TextField("İçerik")
    date = models.DateTimeField("Gönderilme Tarihi", default=timezone.now())
    likes = models.IntegerField("Beğeni Sayısı", default=0)
    yazar = models.ForeignKey(Yazar, on_delete=models.CASCADE)
    yazi_image = models.ImageField("Yazı Footğrafı", blank=True)

    def __str__(self):
        return self.title

    def increment(self):
        # Beğenilerin arttırılmasını sağlayan metodumuz
        self.likes += 1
        try:
            self.save()
        except Exception as e:
            print("Error", e.__cause__)
