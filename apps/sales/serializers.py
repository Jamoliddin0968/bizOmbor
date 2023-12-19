from rest_framework import serializers
from .models import Sale,SaleItem
from django.db import transaction

class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = "__all__"

class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True,source='sale_items')
    class Meta:
        fields = ('id','date','discount','cash','without_cash','total_summa','items')
        model = Sale


# create qismi uchun


class SaleItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = ('product', 'price', 'amount', 'total')



class SaleCreateSerializer(serializers.Serializer):

    items = SaleItemCreateSerializer(many=True)
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
            print(items)
            new_items=[]
            summ = 0
            for item in items:
                temp = SaleItem(sale=sale_object,price = item["price"],product=item['product'],amount=item['amount'],total=item['total'])
                new_items.append(temp)
                summ+=temp.total
            SaleItem.objects.bulk_create(new_items)
            sale_object.total_summa = summ
            print(sale_object,"sdfghjklyoturgfsdvxcbvkgjthrufsdjnsGHdjkfsgdajkhgd")
        return sale_object


