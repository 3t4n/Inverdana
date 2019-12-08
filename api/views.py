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
#Token
class PushTokensViewSet(viewsets.ModelViewSet):
    queryset =  Push.PushToken.objects.all()
    serializer_class = PushTokenSerializer

#User
class UserViewSet(views.UserViewSet):
     def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserSerializer(instance)
        return Response(serializer.data)

#Locations
class WorldBorderViewSet(viewsets.ModelViewSet):
    queryset =  WorldBorder.WorldBorder.objects.all()
    serializer_class = WorldBorderSerializer

#Trees
class TreeViewSet(viewsets.ModelViewSet):
    queryset = Tree.Tree.objects.all()
    serializer_class = TreeSerializer

#Christmas trees
class PineSpecieViewSet(viewsets.ModelViewSet):
    queryset = ChristmasTrees.PineSpecie.objects.all()
    serializer_class = PineSpecieSerializer

class PineStateViewSet(viewsets.ModelViewSet):
    queryset = ChristmasTrees.PineState.objects.all()
    serializer_class = PineStateSerializer

class PineSizeViewSet(viewsets.ModelViewSet):
    queryset = ChristmasTrees.PineSize.objects.all()
    serializer_class = PineSizeSerializer

class PineTreeViewSet(viewsets.ModelViewSet):
    queryset = ChristmasTrees.PineTree.objects.all()
    serializer_class = PineTreeSerializer

class PineLoanViewSet(viewsets.ModelViewSet):
    queryset = ChristmasTrees.PineLoan.objects.all()
    serializer_class = PineLoanSerializer


#Tree's states
class StatesViewSet(viewsets.ModelViewSet):
    queryset = Tree.TreeState.objects.all()
    serializer_class = TreeState

class TreeStateViewSet(viewsets.ModelViewSet):
    queryset = Tree.HasState.objects.all()
    serializer_class = HasState

#Tree's species
class TreeSpecieViewSet(viewsets.ModelViewSet):
    queryset = Tree.TreeSpecie.objects.all()
    serializer_class = TreeSpecieSerializer

#Qr's
class QRcodeViewSet(viewsets.ModelViewSet):
    queryset = Identifier.QRcode.objects.all()
    serializer_class = QRcodeSerializer

#Photos
class PhotosViewSet(viewsets.ModelViewSet):
    queryset = Photo.Photo.objects.all()
    serializer_class = PhotosSerializer

#Events
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.Event.objects.all()
    serializer_class = EventSerializer

#Feed
class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.Post.objects.all()
    serializer_class = FeedSerializer
    filter_backends = (filters.OrderingFilter,)
    filter_mappings = {
        'user': 'user',
        'dateCreated': 'dateCreated',
    }

#Suggestions
class SuggestionsViewSet(viewsets.ModelViewSet):
    queryset = Suggestions.Suggestion.objects.all()
    serializer_class = SuggestionSerializer

#class StatesViewSet(viewsets.ModelViewSet):
#    queryset = Tree.TreeState.objects.all()
    #serializer_class = SuggestionSerializer


#class SharesViewSet(FiltersMixin,viewsets.ModelViewSet):
#Shares
class SharesViewSet(viewsets.ModelViewSet):

    queryset = Tree.Share.objects.all()
    serializer_class = ShareSerializer
    filter_backends = (filters.OrderingFilter,)
    filter_mappings = {
        'id': 'id',
        'tree_id': 'tree_id',
    }


class AchievementsViewSet(viewsets.ModelViewSet):
    queryset = Achievement.Achievement.objects.all()
    serializer_class = AchievementSerializer

def login(request):
    return render(request, 'login.html')


def logintest():
    return '<h1>prueba</h1>'


@login_required
def home(request):
    return render(request, 'index.html')
