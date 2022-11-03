from rest_framework.viewsets import ModelViewSet

from .models import ContactForm1
from .serializers import ContactForm1Serializer

# Create your views here.

class ContactForm1Viewset(ModelViewSet):
    queryset = ContactForm1.objects.all()
    serializer_class = ContactForm1Serializer