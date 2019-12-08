from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError
from djoser import utils
from djoser.serializers import UserCreateSerializer
from djoser.compat import get_user_email, get_user_email_field_name
from djoser.conf import settings
from drf_extra_fields.fields import Base64ImageField
from .models import *
from users.models import *

##Get the current User Class defined in setting.py
User = get_user_model()

#Token
class PushTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Push.PushToken
        fields = ['id','user_id','token']
    def create(self, validated_data):
        token = Push.PushToken.objects.filter(token=validated_data['token'])
        print(token)
        if token:
            instance = Push.PushToken.objects.get(token=validated_data['token'])
        else:
            instance =  Push.PushToken.objects.create(**validated_data)
        return instance

#Achievement 
class AchievementCatalogSerializer(serializers.ModelSerializer):
    photo_thumbnail = serializers.ImageField(read_only=True)
    class Meta:
        model = Achievement.AchievementCatalog
        fields = ['name','desc','photo_thumbnail']


class AchievementSerializer(serializers.ModelSerializer):
    achievement_id = AchievementCatalogSerializer()
    class Meta:
        model = Achievement.Achievement
        fields = ['dateCreated','achievement_id']

#Qr
class QRcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identifier.QRcode
        fields = ['status', 'string',
                  #'code',
                  'tree_id']


#Preferences
class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference.Preference
        fields = ['push_notifications_trees', 'push_notifications_events']


#Places
class WorldBorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldBorder.WorldBorder
        fields = ['iso2', 'name']


#User's info
class ContactSerializer(serializers.ModelSerializer):
    photo = Base64ImageField()

    class Meta:
        model = Contact.Contact
        fields = ['cellphone', 'country', 'birthday', 'photo']


#Trees
class TreeTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree.TreeTip
        fields = ['title', 'tip']


class TreeSpecieSerializer(serializers.ModelSerializer):
    tips = TreeTipSerializer(many=True, read_only=True)

    class Meta:
        model = Tree.TreeSpecie
        fields = ['id', 'commonname', 'tips']


class TreeState(serializers.ModelSerializer):
    class Meta:
        model = Tree.TreeState
        fields = ['id', 'name']


class TreeHasState(serializers.ModelSerializer):
    state = TreeState(many=False)

    class Meta:
        model = Tree.HasState
        fields = ['dateCreated', 'state']


class HasState(serializers.ModelSerializer):
    state = TreeState(many=False,read_only=True )
    photo_thumbnail = serializers.ImageField(read_only=True)
    photo = Base64ImageField()

    class Meta:
        model = Tree.HasState
        fields = ['state', 'tree', 'photo', 'photo_thumbnail', 'description']


#Events
class EventSerializer(serializers.ModelSerializer):
    photo_thumbnail = serializers.ImageField()
    photo = Base64ImageField()

    class Meta:
        model = Event.Event
        fields = ['name', 'info', 'photo_thumbnail', 'photo', 'initial_date']
        use_natural_foreign_keys = True
        use_natural_primary_keys = True


#Feed
class FeedSerializer(serializers.ModelSerializer):
    photo_thumbnail = serializers.ImageField(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    photo = Base64ImageField()

    class Meta:
        model = Feed.Post
        fields = ['user', 'username', 'info', 'photo_thumbnail', 'photo', 'dateCreated']


#Suggestions
class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions.Suggestion
        fields = ['title', 'description']


#Photos
class PhotoSerializer(serializers.ModelSerializer):
    photo_thumbnail = serializers.ImageField()

    class Meta:
        model = Photo.Photo
        fields = ['id', 'photo', 'photo_thumbnail']


class PhotosSerializer(serializers.ModelSerializer):
    photo = Base64ImageField()

    class Meta:
        model = Photo.Photo
        fields = ['id', 'photo', 'tree_id']


#Tree serializer
class TreeSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, required=False, read_only=True)
#   specie_id = TreeSpecieSerializer(many=False,read_only=True)
    states = TreeHasState(many=True, read_only=True)
    specie = serializers.CharField(source='specie_id.commonname', read_only=True)

    class Meta:
        model = Tree.Tree
        fields = ['id', 'specie_id', 'name', 'age', 'identifiers', 'photos', 'point', 'x', 'y', 'states', 'specie']


#Christmas Pines
class PineSpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChristmasTrees.PineSpecie
        fields = ['specie_id', 'sciname']


class PineStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChristmasTrees.PineState
        fields = ['name']


class PineSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChristmasTrees.PineSize
        fields = ['size']


class PineTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChristmasTrees.PineTree
        fields = ['specie_id', 'state', 'size']


class PineLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChristmasTrees.PineLoan
        fields = ['user_id', 'tree_id', 'location', 'price']


#Trees related to users
class ShareSerializer(serializers.ModelSerializer):
    tree = TreeSerializer(many=False, read_only=True)
    tree_id = serializers.IntegerField(source='tree.id')

    class Meta:
        model = Tree.Share
        fields = ['user_id', 'id', 'dateCreated', 'dateModified', 'percentage', 'owner', 'tree_id', 'tree']

    def create(self, validated_data):
        print(validated_data)
        trees = Tree.Share.objects.filter(user_id=validated_data['user_id']).count()
        if trees == 0:
            achievement =  Achievement.AchievementCatalog.objects.get(pk=1)
            Achievement.Achievement.objects.create(user_id=validated_data['user_id'],achievement_id=achievement)
        print(trees)
        tree = Tree.Tree.objects.get(pk=validated_data.pop('tree')['id'])
        instance = Tree.Share.objects.create(tree=tree,**validated_data)
        return instance


#Clans
class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clan.MemberShip
        fields = ['clan_id', 'date_joined']


#Users
class UserSerializer(serializers.ModelSerializer):
    preferences = PreferenceSerializer()
    info = ContactSerializer()
    shares = ShareSerializer(many=True)
    clans = MembershipSerializer(many=True)
    achievements = AchievementSerializer(many=True)
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + tuple(['id', 'username', 'info', 'preferences', 'shares','achievements', 'first_name', 'last_name', 'clans'])
        read_only_fields = (settings.LOGIN_FIELD,)

    def update(self, instance, validated_data):
        email_field = get_user_email_field_name(User)
        if settings.SEND_ACTIVATION_EMAIL and email_field in validated_data:
            instance_email = get_user_email(instance)
            if instance_email != validated_data[email_field]:
                instance.is_active = False
                instance.save(update_fields=["is_active"])
        return super().update(instance, validated_data)


class UserCreateSerializerCustomFields(UserCreateSerializer):
    info = ContactSerializer(read_only=False)

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            User._meta.pk.name,
            "password",
            'first_name',
            'last_name',
            'info',
        )

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
            print(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user
    def validate(self, attrs):
        #Falta hacer verificacion :)
        return attrs
    def perform_create(self, validated_data):
        contact_data = validated_data.pop('info')
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            validated_data['info'] = Contact.Contact.objects.create(user_id=user,**contact_data)
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
        return user
