from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import SAFE_METHODS

from .models import MyUser, UserProfile
from .serializers import MyUserSafeSerializer, MyUserSerializer, UserProfileSerializer, UserProfileSafeSerializer

# Create your views here.

class MyUserViewsets(ModelViewSet):
    queryset = MyUser.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return MyUserSafeSerializer
        return MyUserSerializer


class UserProfileViewsets(ModelViewSet):
    queryset = UserProfile.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return UserProfileSafeSerializer
        return UserProfileSerializer