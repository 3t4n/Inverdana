from django.shortcuts import render
from django.contrib.auth.models import User
from djoser import views
from .serializers import *
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers, serializers, viewsets


User = get_user_model()

class UserViewSet(views.UserViewSet):
     def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserSerializer(instance)
        return Response(serializer.data)

class CountryViewSet(viewsets.ModelViewSet):
    pass

def login(request):
    return render(request, 'login.html')


def logintest():
    return '<h1>prueba</h1>'


@login_required
def home(request):
    return render(request, 'home.html')
