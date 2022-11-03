from rest_framework.serializers import ModelSerializer

from .models import ContactForm1


class ContactForm1Serializer(ModelSerializer):

    class Meta:
        model = ContactForm1
        fields = "__all__"

