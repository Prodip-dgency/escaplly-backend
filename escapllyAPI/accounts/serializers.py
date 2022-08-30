from rest_framework.serializers import ModelSerializer

from .models import MyUser, UserProfile


class MyUserSerializer(ModelSerializer):

    class Meta:
        model = MyUser
        fields = "__all__"
        depth = 2


class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"
        depth = 2