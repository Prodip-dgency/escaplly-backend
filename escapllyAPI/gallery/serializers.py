from rest_framework.serializers import ModelSerializer

from .models import GalleryItem
from accounts.serializers import MyUserCustomSerializer


class GallerySerializers(ModelSerializer):

    class Meta:
        model = GalleryItem
        fields = "__all__"


class GallerySafeSerializers(ModelSerializer):
    user = MyUserCustomSerializer()

    class Meta:
        model = GalleryItem
        fields = "__all__"
