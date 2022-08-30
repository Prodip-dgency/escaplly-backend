from rest_framework.serializers import ModelSerializer

from .models import Gallery


class GallerySerializers(ModelSerializer):

    class Meta:
        model = Gallery
        fields = "__all__"
        depth = 2
