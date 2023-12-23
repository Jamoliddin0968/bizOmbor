from rest_framework import serializers

from .models import Cashbox
class CashBoxSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model=Cashbox