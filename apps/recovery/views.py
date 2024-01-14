from rest_framework.generics import CreateAPIView

from apps.recovery.models import Recovery
from apps.recovery.serializers import RecoverySerializer


class RecoveryCreateApiView(CreateAPIView):
    queryset = Recovery.objects.all()
    serializer_class = RecoverySerializer
