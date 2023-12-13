from django.shortcuts import render

from apps.categories.serializers import CategorySerializer
from apps.categories.models import Category
from rest_framework import viewsets
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
