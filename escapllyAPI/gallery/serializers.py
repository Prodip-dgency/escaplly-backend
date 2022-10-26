from rest_framework.serializers import ModelSerializer

from .models import GalleryItem


class GallerySerializers(ModelSerializer):

    class Meta:
        model = GalleryItem
        fields = "__all__"
