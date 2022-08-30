from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . views import MyUserViewsets, UserProfileViewsets


router = DefaultRouter()
router.register('accounts', MyUserViewsets, basename='account')
router.register('user-profile', UserProfileViewsets, basename='user-profile')


urlpatterns = [
    path('viewset/', include(router.urls))
]

