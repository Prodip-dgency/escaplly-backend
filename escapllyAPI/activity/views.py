from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS

from .models import Activity, ActivityProfile, Difficulty
from .serializers import ActivitySerializer, ActivitySafeSerializer, ActivityProfileSerializer, ActivityProfileSafeSerializer, DifficultySerializer, ActivityProfileCustomSerializer


# Create your views here.

class ActivityViewsets(ModelViewSet):
    queryset = Activity.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ActivitySafeSerializer
        return ActivityProfileSafeSerializer

class ActivityProfileViewsets(ModelViewSet):
    queryset = ActivityProfile.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ActivityProfileSafeSerializer
        return ActivityProfileSerializer

class DifficultyViewsets(ModelViewSet):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer


class ActivityCustomAPIViewset(ViewSet):

    def list(self, request):
        queryset = ActivityProfile.objects.all()
        serializer = ActivityProfileCustomSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ActivityProfile.objects.all()
        activity = get_object_or_404(queryset, pk=pk)
        serializer = ActivityProfileCustomSerializer(activity, context={'request': request})
        return Response(serializer.data)