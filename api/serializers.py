from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError
from djoser import utils
from  djoser.serializers import UserCreateSerializer
from djoser.compat import get_user_email, get_user_email_field_name
from djoser.conf import settings
from .models import *

##Get the current User Class defined in setting.py
User = get_user_model()

class QRcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identifier.QRcode
        fields = ['status','string','code','tree_id']

class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
            model = Preference.Preference
            fields = ['push_notifications_trees','push_notifications_events']

class WorldBorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldBorder.WorldBorder
        fields = ['iso2','name']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact.Contact
        fields = ['address1', 'address2', 'cellphone','country','birthday']


class TreeSpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree.TreeSpecie
        fields = ['id','commonname']

class PhotoSpecieSerializer(serializers.ModelSerializer):
    photo_thumbnail = serializers.ImageField()
    class Meta:
        model = Photo.Photo
        fields = ['id','photo','photo_thumbnail']

class TreeSerializer(serializers.ModelSerializer):
    photos = PhotoSpecieSerializer(many=True)
    specie_id = TreeSpecieSerializer(many=False)
    identifiers = QRcodeSerializer(many=True)
    class Meta: 
        model = Tree.Tree
        fields = ['id','specie_id','name','age','identifiers','photos','point']
class ShareSerializer(serializers.ModelSerializer):
    tree = TreeSerializer(many=False)
    class Meta:
        model = Tree.Share
        fields = ['id','dateCreated','dateModified','percentage','owner','tree']

class UserSerializer(serializers.ModelSerializer):
    preferences = PreferenceSerializer()
    info = ContactSerializer()
    shares = ShareSerializer(many=True)
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + tuple(['id','username','info','preferences','shares'])
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
