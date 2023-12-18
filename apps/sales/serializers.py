from rest_framework import serializers
from .models import Sale,SaleItem
from django.db import transaction

class SaleItemSerializer(serializers.ModelSerializer):
    sale = serializers.IntegerField(read_only=True)
    class Meta:
        model = SaleItem
        fields = "__all__"


class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True,source='sale_items')
    class Meta:
        fields = ('date','discount','cash','without_cash','total_summa','items')
        model = Sale

class SaleCreateSerializer(serializers.Serializer):
    items = SaleItemSerializer(many=True)
    discount = serializers.IntegerField(min_value=0)
    cash = serializers.IntegerField(min_value=0)
    without_cash = serializers.IntegerField(min_value=0)

    def create(self, validated_data):
        sale_object = None
        with transaction.atomic():
            discount = validated_data.pop('discount')
            cash = validated_data.pop('cash')
            without_cash=validated_data.pop('without_cash')
            sale_object = Sale.objects.create(discount=discount,cash=cash,without_cash=without_cash)
            items = validated_data.pop('items')
            new_items=[]
            for item in items:
                temp = SaleItem(sale=item["sale"],price = items["price"],product=item['product'],amount=item['amount'],
                                total=item['total'])
                new_items.append(temp)
            SaleItem.objects.bulk_create(new_items)
        return sale_object


