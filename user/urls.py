from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("sign-up", views.sign_up, name="signup"),
    path("", views.profile, name="profile"),
    path("create-post", views.create_yazi, name="yeni_yazi"),
    path("yazilar", views.show_yazis, name="yazi_galeri"),
    path("yazi/<str:id>", views.show_yazi, name="yazi"),
    path("kategori", views.add_category, name="kategori_ekle"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
