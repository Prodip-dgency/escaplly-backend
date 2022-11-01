from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ActivityViewsets, ActivityProfileViewsets, DifficultyViewsets, ActivityCustomAPIViewset, ActivityThemeViewset, ActivityTypeViewset

app_name = 'activity'

router = DefaultRouter()
router.register('activity', ActivityViewsets, basename='activity')
router.register('activityprofile', ActivityProfileViewsets, basename='activityprofile')
router.register('difficulty', DifficultyViewsets, basename='difficulty')
router.register('activity-theme', ActivityThemeViewset, basename='activity_theme')
router.register('activity-type', ActivityTypeViewset, basename='activity_type')
router.register('custom-activity-profile-api', ActivityCustomAPIViewset, basename='customapi')

urlpatterns = [
    path('viewset/', include(router.urls)),
]
