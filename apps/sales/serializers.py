from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.recovery.serializers import RecoverySerializer
from apps.store_users.models import StoreUser
from .models import Sale, SaleItem
from ..recovery.models import RecoveryItem, Recovery


class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True, source='sale_items')

    class Meta:
        fields = ('id', 'date', 'discount', 'cash', 'without_cash', 'total_summa', 'items', 'store', 'user')
        model = Sale


class SaleItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = ('product', 'price', 'amount', 'total')


class SaleCreateSerializer(serializers.Serializer):
    items = SaleItemCreateSerializer(many=True)
    recovery = RecoverySerializer()
    discount = serializers.IntegerField(min_value=0)
    cash = serializers.IntegerField(min_value=0)
    without_cash = serializers.IntegerField(min_value=0)

    def create(self, validated_data):
        sale_object = None
        with transaction.atomic():
            user = self.context['request'].user
            store_user = StoreUser.objects.filter(user=user).first()
            if not store_user:
                raise ValidationError({"message": "You don't permission for store"})
            discount = validated_data.pop('discount')
            cash = validated_data.pop('cash')
            without_cash = validated_data.pop('without_cash')
            store = store_user.store
            sale_object = Sale.objects.create(discount=discount, cash=cash, without_cash=without_cash, user=user,
                                              store=store)
            items = validated_data.pop('items')
            new_items = []
            summ = 0
            for item in items:
                temp = SaleItem(sale=sale_object, price=item["price"], product=item['product'], amount=item['amount'],
                                total=item['total'])
                new_items.append(temp)
                summ += temp.total
            SaleItem.objects.bulk_create(new_items)
            sale_object.total_summa = summ

            user = self.context['request'].user

            items = validated_data.pop('items')
            if items:
                recovery = Recovery.objects.create(sale=sale_object, user=user)
                for item in items:
                    RecoveryItem.objects.create(**item, recovery=recovery)

        return sale_object
