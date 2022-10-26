from rest_framework.serializers import ModelSerializer

from .models import Activity, ActivityProfile, Difficulty
from company.models import Company, CompanyProfile
from gallery.serializers import GallerySerializers

class ActivitySerializer(ModelSerializer):

    class Meta:
        model = Activity
        fields = "__all__"


class DifficultySerializer(ModelSerializer):
    
    class Meta:
        model = Difficulty
        fields = "__all__"


class ActivityProfileSerializer(ModelSerializer):

    class Meta:
        model = ActivityProfile
        fields = "__all__"
        depth = 3



class ActivityProfileCustomSerializer(ModelSerializer):

    class CompanyProfileSerializer(ModelSerializer):
        profile_image = GallerySerializers()

        class Meta:
            model = CompanyProfile
            fields = [
                'id', 
                'title', 
                'city', 
                'state',
                'country',
                'profile_image'
            ]

    activity = ActivitySerializer()
    company_profile = CompanyProfileSerializer(source='getCompanyProfile')
    difficulty = DifficultySerializer()
    main_image = GallerySerializers()
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
            'main_image',
            'gallery'
        ]



