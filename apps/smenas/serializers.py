from rest_framework.serializers import ModelSerializer

from .models import Smena


class SmenaSerializer(ModelSerializer):
    class Meta:
        model = Smena
        fields = "__all__"
