from rest_framework.serializers import ModelSerializer
from .models import StoreUser
from apps.users.serializers import UserSerializer


class StoreUserCreateSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        fields = "__all__"
        model=StoreUser

    def create(self, validated_data):
        user:UserSerializer = validated_data.get('user')
        user = UserSerializer(data=user)
        user.is_valid(raise_exception=True)
        print(validated_data)
        store_user=StoreUser.objects.create(user_id=user.id,store_id=validated_data.get('user'))
