from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index2, name="index2"),
    path("home/main/", views.index3, name="index3")
]