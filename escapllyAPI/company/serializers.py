from pyexpat import model
from rest_framework.serializers import ModelSerializer

from .models import Company, CompanyProfile


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
