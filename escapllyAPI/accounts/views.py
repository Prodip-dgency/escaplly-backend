from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import MyUser, UserProfile
from .serializers import MyUserSerializer, UserProfileSerializer

# Create your views here.

class MyUserViewsets(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class UserProfileViewsets(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    