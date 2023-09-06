from django.db import models
from django.utils import timezone

# Create your models here.
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
