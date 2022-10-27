from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Activity, ActivityProfile, Difficulty
from .serializers import ActivitySerializer, ActivityProfileSerializer, DifficultySerializer, ActivityProfileCustomSerializer


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


class ActivityCustomAPIView(APIView):
    
    def get(self, request, fromat=None):
        activity = Activity.objects.get(pk=6)
        activities = activity.title
        return Response(activities)


# class ActivityCustomAPIViewset(ViewSet):

#     def list(self, request):
#         queryset = ActivityProfile.objects.all()
#         serializer = ActivityProfileSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         print('Passed')
#         queryset = ActivityProfile.objects.all()
#         activity = get_object_or_404(queryset, pk=pk)
#         serializer = ActivityProfileSerializer(activity)
#         return Response(serializer.data)


class ActivityCustomAPIViewset(ViewSet):

    def list(self, request):
        queryset = ActivityProfile.objects.all()
        serializer = ActivityProfileCustomSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print('Passed')
        queryset = ActivityProfile.objects.all()
        activity = get_object_or_404(queryset, pk=pk)
        serializer = ActivityProfileCustomSerializer(activity, context={'request': request})
        return Response(serializer.data)