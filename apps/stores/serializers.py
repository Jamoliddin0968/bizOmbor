from rest_framework.serializers import ModelSerializer
from .models import Store
from rest_framework import serializers

class StoreSerializer(ModelSerializer):


    class Meta:
        model = Store
        exclude = ("manager",)
