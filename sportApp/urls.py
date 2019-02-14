from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getSports, name="sport"),
    path('test/',views.test),
    ]
