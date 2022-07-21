from django.contrib import admin
from django.urls import path
from instagram import views

urlpatterns = [
    path("", views.index, name="home"),
    path("private-profile", views.username, name="username"),
    path("profile", views.profile, name="profile"),
    path("login", views.login, name="login"),
]
