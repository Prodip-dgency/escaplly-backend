from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ContactForm1Viewset

app_name = 'contactform'

router = DefaultRouter()
router.register('contact-from1', ContactForm1Viewset, basename='ContactForm1')


urlpatterns = [
    path('viewsets/', include(router.urls))
]
