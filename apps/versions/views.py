from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
from rest_framework.viewsets import GenericViewSet

from .models import Version
from .serializers import VersionSerializer


class VersionViewSet(GenericViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer

    @action(detail=False, methods=['get'], url_path='new_versions/(?P<version_id>[^/.]+)')
    def get_new_versions(self, request, version_id=None):
        if version_id is not None:
            try:
                version_id = int(version_id)
                versions = Version.objects.filter(id__gt=version_id)
                serializer = VersionSerializer(versions, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ValueError:
                return Response({"error": "Invalid version_id"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "version_id is required"}, status=status.HTTP_400_BAD_REQUEST)
