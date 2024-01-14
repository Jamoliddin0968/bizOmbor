from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.store_users.models import StoreUser
from apps.recovery.models import Recovery,RecoveryItem



class RecoveryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecoveryItem
        exclude = ('sale',)

class RecoverySerializer(serializers.ModelSerializer):
    items = RecoveryItemSerializer(many=True)
    class Meta:
        model = Recovery
        fields = "__all__"
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        recovery = None
        with transaction.atomic():
            user = self.context['request'].user
            sale = validated_data.get('sale')
            store_user = StoreUser.objects.filter(user=user).first()
            if not store_user:
                raise ValidationError({"message":"You don't permission for store"})
            items = validated_data.pop('items')
            if items:
                recovery = Recovery.objects.create(sale=sale, user=user)
                for item in items:
                    RecoveryItem.objects.create(**item,recovery=recovery)
        return recovery


