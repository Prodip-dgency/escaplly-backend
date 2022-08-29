from django.shortcuts import render

from rest_framework import viewsets

from .models import Activity, ActivityProfile, Difficulty, Accessibility
from .serializers import ActivitySerializer, ActivityProfileSerializer, DifficultySerializer, AccessibilitySerializer


# Create your views here.

class ActivityViewsets(viewsets.ModelViewSet):

    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ActivityProfileViewsets(viewsets.ModelViewSet):
    queryset = ActivityProfile.objects.all()
    serializer_class = ActivityProfileSerializer


class DifficultyViewsets(viewsets.ModelViewSet):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer


class AccessibilityViewsets(viewsets.ModelViewSet):
    queryset = Accessibility.objects.all()
    serializer_class = AccessibilitySerializer