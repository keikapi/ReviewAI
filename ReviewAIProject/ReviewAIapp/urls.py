from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="Index"),
    path('userprompt/', views.userpromptview.as_view(), name="userprompt"),
]