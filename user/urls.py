from django.urls import path, include
from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("sign-up", views.sign_up, name="signup"),
    path("profile", views.profile, name="profile"),
    path("create-post", views.create_yazi, name="yeni_yazi"),
    path("yazilar", views.show_yazis, name="yazi_galeri"),
    path("yazi/<str:id>", views.show_yazi, name="yazi"),
]
