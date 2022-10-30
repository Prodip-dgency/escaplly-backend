from email.policy import default
from rest_framework.serializers import ModelSerializer

from .models import GalleryItem
from accounts.serializers import MyUserCustomSerializer


class GallerySerializers(ModelSerializer):

    class Meta:
        model = GalleryItem
        fields = "__all__"

    def get_fields(self):
        this_model_name = 'GalleryItem'
        fields = super().get_fields()

        exclude_fields_dictionary = self.context.get('exclude_fields', [])

        if exclude_fields_dictionary:
            exclude_fields = exclude_fields_dictionary.get(this_model_name, [])
            for field in exclude_fields:
                fields.pop(field, default=None)
        return fields


class GallerySafeSerializers(ModelSerializer):
    user = MyUserCustomSerializer()

    class Meta:
        model = GalleryItem
        fields = "__all__"
