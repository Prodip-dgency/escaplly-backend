from rest_framework.serializers import ModelSerializer

from .models import Activity, ActivityProfile, Difficulty

class ActivitySerializer(ModelSerializer):

    class Meta:
        model = Activity
        fields = "__all__"
        depth = 2


class DifficultySerializer(ModelSerializer):
    
    class Meta:
        model = Difficulty
        fields = "__all__"


class ActivityProfileSerializer(ModelSerializer):

    class Meta:
        model = ActivityProfile
        fields = "__all__"
        depth = 3



