from rest_framework.viewsets import ModelViewSet

from .models import Smena
from .serializers import SmenaSerializer


class SmenaViewSet(ModelViewSet):
    serializer_class = SmenaSerializer
    queryset = Smena.objects.all()
