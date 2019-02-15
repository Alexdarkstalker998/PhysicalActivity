from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="sport"),
    path('test/',views.test),
    path('schedule/', views.schedule),
    path('admin/', views.admin),
    path('getlesson/',views.getlesson),
    path('dolesson/', views.dolesson),
    path('testtest/',views.testtest),
    path('coschedule/',views.coschedule),
    path('colesson/',views.colesson),
    path('copoints/',views.copoints),
    ]
