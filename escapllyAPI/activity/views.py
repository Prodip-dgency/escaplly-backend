from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Activity, ActivityProfile, Difficulty
from .serializers import ActivitySerializer, ActivityProfileSerializer, DifficultySerializer


# Create your views here.

class ActivityViewsets(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ActivityProfileViewsets(ModelViewSet):
    queryset = ActivityProfile.objects.all()
    serializer_class = ActivityProfileSerializer


class DifficultyViewsets(ModelViewSet):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer


