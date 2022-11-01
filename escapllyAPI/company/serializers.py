from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Company, CompanyProfile, Accessibility, GuideLine
from activity.models import ActivityProfile, Difficulty
from accounts.serializers import MyUserCustomSerializer, MyUserSerializer
from gallery.serializers import GallerySerializers


# Serializers for Company model
class CompanySerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"



class CompanySafeSerializer(ModelSerializer):
    user = MyUserSerializer()

    class Meta:
        model = Company
        fields = "__all__"



# Serializers for CompanyProfile model
class CompanyProfileSerializer(ModelSerializer):

    class Meta:
        model = CompanyProfile
        fields = "__all__"



class CompanyProfileSafeSerializer(ModelSerializer):
    company = CompanySerializer()
    profile_image = GallerySerializers()
    cover_image = GallerySerializers()

    class Meta:
        model = CompanyProfile
        fields = "__all__"


# Serializers for Accessibility model
class AccessibilitySerializer(ModelSerializer):
    
    class Meta:
        model = Accessibility
        fields = "__all__"

# Serializers for GuideLine model
class GuideLineSerializer(ModelSerializer):

    class Meta:
        model = GuideLine
        fields = "__all__"


# Custom Serializers for CompanyProfile model
class DifficultySerializer(ModelSerializer):

    class Meta:
        model = Difficulty
        fields = ["title"]

class CompanyDetailsSerializer(ModelSerializer):

    class ActivityProfileSerializer(ModelSerializer):
        main_image = GallerySerializers()
        difficulty = DifficultySerializer()

        class Meta:
            model = ActivityProfile
            fields = [
                        'main_image', 
                        'minimum_participant',
                        'maximum_participant',
                        'duration',
                        'difficulty',
                        'mimimum_age',
                        'title',
                        'short_description',
                        'price'
                    ]
    
    activity_profiles  = ActivityProfileSerializer(source='getActivities.activitie_profiles', many=True)
    available_escape_game  = serializers.IntegerField(source='getActivities.total_activities')
    lowest_age  = serializers.IntegerField(source='getActivities.lowest_age')
    average_minimum_participant  = serializers.IntegerField(source='getActivities.average_minimum_participant')
    average_maximum_participant  = serializers.IntegerField(source='getActivities.average_maximum_participant')
    highest_accompany_age  = serializers.IntegerField(source='getActivities.highest_accompany_age')
    average_game_duration  = serializers.IntegerField(source='getActivities.average_game_duration')
    gallery = GallerySerializers(source='getAllRelatedGalleryItems', many=True)
    profile_image = GallerySerializers()
    cover_image = GallerySerializers()

    class Meta:
        model = CompanyProfile
        fields = [
            'id',
            'city', 
            'state', 
            'title', 
            'cover_image',
            'profile_image',
            'available_escape_game',
            'about',
            'address_line',
            'website_url',
            'phone_number', 
            'lowest_age',
            'average_game_duration',
            'highest_accompany_age',
            'average_maximum_participant',
            'average_minimum_participant',
            'activity_profiles', 
            'gallery',
        ]


# Custom Serializers for CompanyProfile model

