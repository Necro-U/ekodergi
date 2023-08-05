from django.db import models
import datetime

# Create your models here.


class Yazi(models.Model):
    isim = models.CharField("Yazar ismi", max_length=30)
    title = models.CharField("Yazı Başlığı", max_length=100)
    icerik = models.TextField("İçerik")
    date = models.DateTimeField("Gönderilme Tarihi", default=datetime.datetime.now())

    def __str__(self):
        return self.isim


class Begeni(models.Model):
    count = models.IntegerField("Begeni", default=0)
    yazi = models.ForeignKey(Yazi, on_delete=models.CASCADE)

    def increase(self):
        self.count += 1
        print("sea" + self.count)
