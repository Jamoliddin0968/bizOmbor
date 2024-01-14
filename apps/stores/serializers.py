from rest_framework.serializers import ModelSerializer

from .models import Store


class StoreSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"
        extra_kwargs = {
            'manager': {'read_only': True}  # Assuming you don't want to allow image update via API
        }
