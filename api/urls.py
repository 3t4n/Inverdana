"""API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from api import views
from django.conf.urls import url, include
from djoser import views
from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'qrcodes', QRcodeViewSet)
router.register(r'trees', TreeViewSet)
router.register(r'species', TreeSpecieViewSet)
router.register(r'shares', SharesViewSet)
router.register(r'photos', PhotosViewSet)
router.register(r'worldborders', WorldBorderViewSet)

urlpatterns = [
    #Ejemplo
    path('users/', views.UserViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
    'put': 'update',
    'patch': 'partial_update'
    })),
    path('users/me/', UserViewSet.as_view({
    'get': 'me',
    'delete': 'me',
    'put': 'me',
    'patch': 'me'
    })),
    
    path('auth/login/', views.TokenCreateView.as_view()),
    path('auth/logout/', views.TokenDestroyView.as_view()),
#    url(r'^auth/', include('djoser.urls')),
#    url(r'^auth/', include('djoser.urls.jwt')),
#    url(r'^auth/', include('djoser.urls.authtoken')),

    ] + router.urls
