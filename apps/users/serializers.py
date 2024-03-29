from rest_framework.serializers import ModelSerializer, CharField

from .models import User


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True,
                         style={'input_type': 'password'})

    def create(self, validated_data):
        user = super().create(validated_data)
        pswd = validated_data.get("password")
        user.set_password(pswd)
        user.save()
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
