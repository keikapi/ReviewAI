from django.urls import path

from . import views

urlpatterns = [
    path("", views.firstmethod, name="firstmethod"),
]