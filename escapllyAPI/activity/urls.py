from atexit import register
import re
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ActivityViewsets, ActivityProfileViewsets, DifficultyViewsets, AccessibilityViewsets

router = DefaultRouter()
router.register('activity', ActivityViewsets, basename='activity')
router.register('activityprofile', ActivityProfileViewsets, basename='activityprofile')
router.register('difficulty', DifficultyViewsets, basename='difficulty')
router.register('accessibility', AccessibilityViewsets, basename='accessibility' )

urlpatterns = [
    path('viewset/', include(router.urls))    
]
