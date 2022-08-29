from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CompanyViewset, CompanyProfileViewset, CompanyHome

router = DefaultRouter()
router.register('company', CompanyViewset, basename='company')
router.register('company-profile', CompanyProfileViewset, basename='company-profile')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('', CompanyHome, name='Home')
]
