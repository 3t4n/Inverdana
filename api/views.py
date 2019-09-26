from django.shortcuts import render
from django.contrib.auth.models import User
from djoser import views
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response



User = get_user_model()

class UserViewSet(views.UserViewSet):
     def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserSerializer(instance)
        return Response(serializer.data)

