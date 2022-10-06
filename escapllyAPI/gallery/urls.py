from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GalleryViewsets

app_name = 'gallery'

router = DefaultRouter()
router.register('gallery', GalleryViewsets, basename='gallery')

urlpatterns = [
    path('viewset/', include(router.urls))
]
