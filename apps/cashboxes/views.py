from django.shortcuts import render

# Create your views here.
from .serializers import CashBoxSerializer
from .models import CashBox
from rest_framework import viewsets
class CashBoxViewSet(viewsets.ModelViewSet):
    queryset = CashBox.objects.all()
    serializer_class = CashBoxSerializer
