from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Gallery
from .serializers import GallerySerializers

# Create your views here.

class GalleryViewsets(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers
    
