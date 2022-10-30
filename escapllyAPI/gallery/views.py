from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import SAFE_METHODS

from .models import GalleryItem
from .serializers import GallerySerializers, GallerySafeSerializers

# Create your views here.

class GalleryViewsets(ModelViewSet):
    queryset = GalleryItem.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return GallerySafeSerializers
        return GallerySerializers
