# from rest_framework.fields import
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, CharField, IntegerField

from apps.users.models import User
from apps.users.serializers import UserSerializer
from .models import StoreUser
from ..stores.models import Store


class StoreUserCreateSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True,
                         style={'input_type': 'password'})

    def validate_store(self, value):
        try:
            store = Store.objects.get(id=value)
            current_user = self.context['request'].user
            if not store.manager == current_user:
                raise serializers.ValidationError("You don't have permission")
        except Store.DoesNotExist:
            raise serializers.ValidationError("Invalid Store ID")
        return value

    class Meta:
        model = User
        fields = ("id", 'first_name', 'last_name', 'username', "img",
                  "phone", "password", 'store')



class StoreUserSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        fields = '__all__'
        model = StoreUser


class PasswordChangeSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True,
                         style={'input_type': 'password'})

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
            instance.save()
        return super().update(instance, validated_data)

    class Meta:
        model = User
        fields = ("password",)
