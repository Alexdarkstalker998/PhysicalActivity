"""Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('dbadmin/', views.dbview),
    path('sport/', include('sportApp.urls')),
    path('',views.login),
    path('dbadmin/sports/', views.dbsports),
    path('dbadmin/students/',views.dbstudents),
    path('dbadmin/coachs/',views.dbcoachs),
    path('dbadmin/places/',views.dbplaces),
    path('dbadmin/lessons/',views.dblessons),
    path('dbadmin/messages/',views.dbmessages),
    path('edit/',views.lessonedit),
    path('edit/marks/',views.lessonmark),
    path('edit/messages/',views.lessonmessages),
]
