from django.urls import path
from . import views 


urlpatterns = [
    path("anasayfa/", views.index, name="index"),
    path("yazilar/<int:yazi_id>/", views.yazi, name="yazi"),
    path("konular/<int:konu_id>/", views.konu, name="konu"),
    path("login/",views.login,name="giris"),
    path("kayit-ol/",views.sign_up,name="kayitol")
]
