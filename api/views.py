from django.shortcuts import render
from django.contrib.auth.models import User
from djoser import views
from .serializers import *
from .models import *
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers, serializers, viewsets, filters
#from filters.mixins import (FiltersMixin,)

User = get_user_model()

class UserViewSet(views.UserViewSet):
     def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserSerializer(instance)
        return Response(serializer.data)

class WorldBorderViewSet(viewsets.ModelViewSet):
    queryset =  WorldBorder.WorldBorder.objects.all()
    serializer_class = WorldBorderSerializer

class TreeViewSet(viewsets.ModelViewSet):
    queryset = Tree.Tree.objects.all()
    serializer_class = TreeSerializer

class TreeSpecieViewSet(viewsets.ModelViewSet):
    queryset = Tree.TreeSpecie.objects.all()
    serializer_class = TreeSpecieSerializer

class QRcodeViewSet(viewsets.ModelViewSet):
    queryset = Identifier.QRcode.objects.all()
    serializer_class = QRcodeSerializer

class PhotosViewSet(viewsets.ModelViewSet):
    queryset = Photo.Photo.objects.all()
    serializer_class = PhotosSerializer

#Events
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.Event.objects.all()
    serializer_class = EventSerializer

class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.Post.objects.all()
    serializer_class = FeedSerializer

class SuggestionsViewSet(viewsets.ModelViewSet):
    queryset = Suggestions.Suggestion.objects.all()
    serializer_class = SuggestionSerializer

#class SharesViewSet(FiltersMixin,viewsets.ModelViewSet):
class SharesViewSet(viewsets.ModelViewSet):

    queryset = Tree.Share.objects.all()
    serializer_class = ShareSerializer
    filter_backends = (filters.OrderingFilter,)
    filter_mappings = {
        'id': 'id',
        'tree_id': 'tree_id',
    }


def login(request):
    return render(request, 'login.html')


def logintest():
    return '<h1>prueba</h1>'


@login_required
def home(request):
    return render(request, 'index.html')
