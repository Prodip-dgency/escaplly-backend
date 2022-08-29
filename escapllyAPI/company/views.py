from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet


from .models import Company, CompanyProfile
from .serializers import CompanySerialzer, CompanyProfileSerializer


def CompanyHome(request):
    return HttpResponse('<h1>Hello!</h1>')


class CompanyViewset(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerialzer


class CompanyProfileViewset(ModelViewSet):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer

