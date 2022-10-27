from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Company, CompanyProfile, Accessibility, GuideLine
from activity.serializers import ActivityProfileSerializer


class CompanySerialzer(ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"
        depth = 2


class CompanyProfileSerializer(ModelSerializer):

    class Meta:
        model = CompanyProfile
        fields = "__all__"
        depth = 2


class AccessibilitySerializer(ModelSerializer):
    
    class Meta:
        model = Accessibility
        fields = "__all__"


class GuideLineSerializer(ModelSerializer):

    class Meta:
        model = GuideLine
        fields = "__all__"


class CompanyDetailsSerializer(ModelSerializer):
    company = CompanySerialzer()
    activity  = ActivityProfileSerializer(source='getActivities.activities', many=True)
    total_activities  = serializers.IntegerField(source='getActivities.total_activities')

    class Meta:
        model = CompanyProfile
        fields = ['title', 'address_line', 'city', 'state', 'company', 'activity', 'total_activities']


