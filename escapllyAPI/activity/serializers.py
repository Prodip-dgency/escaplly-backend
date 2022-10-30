from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers

from .models import Activity, ActivityProfile, Difficulty
from company.models import CompanyProfile
from company.serializers import CompanySerializer, CompanyProfileSerializer
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
class ActivityProfileCustomSerializer(ModelSerializer):

    # class CompanyProfileSerializer(ModelSerializer):
    #     profile_image = GallerySerializers()

    #     class Meta:
    #         model = CompanyProfile
    #         fields = [
    #             'id', 
    #             'title', 
    #             'city', 
    #             'state',
    #             'country',
    #             'profile_image'
    #         ]

    class GuideLineSerializer(Serializer):
        title = serializers.CharField(max_length=100)
        description = serializers.CharField(max_length=200)

    activity = ActivitySerializer()
    company_profile = CompanyProfileSerializer(source='getCompanyProfile')
    difficulty = DifficultySerializer()
    main_image = GallerySerializers()
    guideline = GuideLineSerializer(many=True)
    gallery = GallerySerializers(source='getAllRelatedGalleryItems', many=True)

    
    class Meta:
        model = ActivityProfile
        fields = [
            'id',
            'title',
            'activity',
            'company_profile',
            'short_description',
            'website_link',
            'storyline',
            'price',
            'minimum_participant',
            'maximum_participant',
            'duration',
            'difficulty',
            'mimimum_age',
            'accompany_age',
            'address',
            'guideline',
            'main_image',
            'guideline',
            'gallery'
        ]



