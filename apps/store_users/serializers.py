# from rest_framework.fields import
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,CharField,IntegerField
from .models import StoreUser
from apps.users.serializers import UserSerializer
from apps.stores.serializers import StoreSerializer
from apps.users.models import User
from ..stores.models import Store


class StoreUserCreateSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True,
                         style={'input_type': 'password'})
    store = IntegerField()

    def validate_store_id(self, value):
        # You can perform validation for the store field here
        try:
            store = Store.objects.get(id=value)
            current_user = self.context['request'].user
            if not store.manager == current_user:
                raise serializers.ValidationError("You don't have permission")
        except Store.DoesNotExist:
            raise serializers.ValidationError("Invalid Store ID")
        return value
    def create(self, validated_data):
        store = validated_data.pop('store')
        user=User.objects.create(**validated_data)
        pswd = validated_data.get("password")
        user.set_password(pswd)
        user.save()
        store_user=StoreUser.objects.create(user=user,store=store)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
            instance.save()
        return super().update(instance, validated_data)

    class Meta:
        model = User
        fields = ("id", 'first_name', 'last_name', 'username', "img",
                  "phone", "is_active", "password")

    class Meta:
        fields = "__all__"
        model=StoreUser

    def create(self, validated_data):
        user:UserSerializer = validated_data.get('user')
        user = UserSerializer(data=user)
        user.is_valid(raise_exception=True)
        user=user.save()
        store_user=StoreUser.objects.create(user=user,store=validated_data.get('store'))

        return store_user


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

