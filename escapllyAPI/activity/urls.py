from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ActivityViewsets, ActivityProfileViewsets, DifficultyViewsets, ActivityCustomAPIView, ActivityCustomAPIViewset

app_name = 'activity'

router = DefaultRouter()
router.register('activity', ActivityViewsets, basename='activity')
router.register('activityprofile', ActivityProfileViewsets, basename='activityprofile')
router.register('difficulty', DifficultyViewsets, basename='difficulty')
router.register('customapi', ActivityCustomAPIViewset, basename='customapi')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('customapi/', ActivityCustomAPIView.as_view(), name='customAPIView') 
]
