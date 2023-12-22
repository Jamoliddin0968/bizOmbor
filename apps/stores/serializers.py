from rest_framework.serializers import ModelSerializer
from .models import Store,StoreUser
from rest_framework import serializers
from apps.users.serializers import WorkerSerializer
class StoreSerializer(ModelSerializer):


    class Meta:
        model = Store
        exclude = ("manager",)


class StoreUserCreateSerializer(ModelSerializer):
    user = WorkerSerializer()
    class Meta:
        fields = "__all__"
        model = StoreUser

    def create(self, validated_data):
        user = validated_data.get('user')
        store = validated_data.get('store')
        user = WorkerSerializer(data=user)
        user.is_valid(raise_exception=True)
        user.save()
        store_user,_ = StoreUser.objects.get_or_create(user=user,store=store)
        return store_user