from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError
from djoser import utils
from djoser.compat import get_user_email, get_user_email_field_name
from djoser.conf import settings
from .models import *

##Get the current User Class defined in setting.py
User = get_user_model()


class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
            model = Preference.Preference
            fields = ['push_notifications_trees','push_notifications_events']

class WorldBorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldBorder.WorldBorder
        fields = ['name']

class ContactSerializer(serializers.ModelSerializer):
    country = WorldBorderSerializer(many=False)
    class Meta:
        model = Contact.Contact
        fields = ['address1', 'address2', 'cellphone','country']


class TreeSpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree.TreeSpecie
        fields = ['id','common name']

class TreeSerializer(serializers.ModelSerializer):
    specie_id = TreeSpecieSerializer(many=False)
    class Meta: 
        model = Tree.Tree
        fields = ['id','name','specie','age','point']

class UserSerializer(serializers.ModelSerializer):
    preferences = PreferenceSerializer()
    info = ContactSerializer()
    shares = TreeSpecieSerializer(many=True)
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
