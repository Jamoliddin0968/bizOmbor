from rest_framework import serializers

from .models import CashBox
class CashBoxSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model=CashBox