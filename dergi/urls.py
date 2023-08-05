from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:yazi_id>/", views.yazi, name="yazi"),
]
