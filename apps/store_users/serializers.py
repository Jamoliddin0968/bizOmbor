# from rest_framework.fields import
from rest_framework.serializers import ModelSerializer,CharField
from .models import StoreUser
from apps.users.serializers import UserSerializer
from apps.stores.serializers import StoreSerializer
from ..users.models import User


class StoreUserCreateSerializer(ModelSerializer):
    user = UserSerializer()
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

