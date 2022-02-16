'''
Author: LetMeFly
Date: 2022-02-02 12:22:43
LastEditors: LetMeFly
LastEditTime: 2022-02-16 11:48:57
'''
"""Diary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.contrib.staticfiles.views import serve
from django.views.generic.base import RedirectView
from Apps import views


urlpatterns = [
    path('', views.html('index.html')),
    path('admin/', admin.site.urls),
    # path('favicon.ico/',serve, {'path': 'Static/Img/favicon.ico'}),
    path('favicon.ico/', RedirectView.as_view(url='/Static/Img/favicon.ico')),
    path('login/', views.login),
    path('AddADiary/', views.add1diary), 
    path('GetAllDiaries/', views.getAllDiaries),
    path('Get1Diary/', views.get1diary),
    path('Del1Diary/', views.del1diary),
    path("try/", views.send1Message_Try),
    path("tryForReminder/", views.autoCheck2Remind_Try),
]
