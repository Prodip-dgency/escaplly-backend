from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers

from .models import Activity, ActivityProfile, Difficulty, ActivityTheme, ActivityType
from company.serializers import CompanySerializer
from gallery.serializers import GallerySerializers


# Serializers for Activity model
class ActivitySerializer(ModelSerializer):

    class Meta:
        model = Activity
        fields = "__all__"


class ActivitySafeSerializer(ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Activity
        fields = "__all__"


# Serializers for Difficulty model
class DifficultySerializer(ModelSerializer):
    
    class Meta:
        model = Difficulty
        fields = "__all__"


# Serializers for ActivityTheme model
class ActivityThemeSerializer(ModelSerializer):
    
    class Meta:
        model = ActivityTheme
        fields = "__all__"


# Serializers for ActivityType model
class ActivityTypeSerializer(ModelSerializer):
    
    class Meta:
        model = ActivityType
        fields = "__all__"


# Serializers for ActivityProfile model
class ActivityProfileSerializer(ModelSerializer):

    class Meta:
        model = ActivityProfile
        fields = "__all__"


class ActivityProfileSafeSerializer(ModelSerializer):
    activity = ActivitySerializer()
    difficulty = DifficultySerializer()
    main_image = GallerySerializers()

    class Meta:
        model = ActivityProfile
        fields = "__all__"


# Serializers for CutsomActivityProfile

class GalleryCustomSerializer(Serializer):
    image = serializers.ImageField()

class ActivityProfileCustomSerializer(ModelSerializer):
    
    class CompanyProfileCustomSerializer(Serializer):
        id = serializers.IntegerField()
        city = serializers.CharField(max_length=100)
        state = serializers.CharField(max_length=100)
        title = serializers.CharField(max_length=200)
        profile_image = GalleryCustomSerializer()
        address_line = serializers.CharField(max_length=200)

    class GuideLineSerializer(Serializer):
        title = serializers.CharField(max_length=100)
        description = serializers.CharField(max_length=200)

    
    class DifficultyCustomSerializer(Serializer):
        title = serializers.CharField(max_length=100)

    company_profile = CompanyProfileCustomSerializer(source='getCompanyProfile')
    difficulty = DifficultyCustomSerializer()
    activity_type = ActivityTypeSerializer()
    activity_theme = ActivityThemeSerializer(many=True)
    guideline = GuideLineSerializer(many=True)
    gallery = GalleryCustomSerializer(source='getAllRelatedGalleryItems', many=True)
    main_image = GalleryCustomSerializer()


    
    class Meta:
        model = ActivityProfile
        fields = [
            'company_profile',
            'id',
            'title',
            'short_description',
            'gallery',
            'storyline',
            'price',
            'minimum_participant',
            'maximum_participant',
            'duration',
            'difficulty',
            # 'website_link',
            'mimimum_age',
            'accompany_age',
            # 'address',
            'guideline',
            'main_image',
            'activity_type',
            'activity_theme'
        ]



