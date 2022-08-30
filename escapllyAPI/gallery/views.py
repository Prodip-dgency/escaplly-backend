from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import GalleryItem
from .serializers import GallerySerializers

# Create your views here.

class GalleryViewsets(ModelViewSet):
    queryset = GalleryItem.objects.all()
    serializer_class = GallerySerializers
    
