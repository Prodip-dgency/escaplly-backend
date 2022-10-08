from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CompanyViewset, CompanyProfileViewset, CompanyHome, AccessibilityViewsets, CompanyDetailsViewsets

app_name = 'company'

router = DefaultRouter()
router.register('company', CompanyViewset, basename='company')
router.register('company-profile', CompanyProfileViewset, basename='company-profile')
router.register('accessibility', AccessibilityViewsets, basename='accessibility' )
router.register('company-details', CompanyDetailsViewsets, basename='company-details')


urlpatterns = [
    path('viewset/', include(router.urls)),
    path('', CompanyHome, name='Home')
]
