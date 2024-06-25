from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="Index"),
    path('userprompt/', views.userpromptview, name="userprompt"),
    path('userprompt/redirect/', views.redirectview, name="redirect"),
]