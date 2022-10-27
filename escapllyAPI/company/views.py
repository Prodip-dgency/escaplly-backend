from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response


from .models import Company, CompanyProfile, Accessibility, GuideLine
from .serializers import CompanySerialzer, CompanyProfileSerializer, AccessibilitySerializer, CompanyDetailsSerializer, GuideLineSerializer


def CompanyHome(request):
    return HttpResponse('<h1>Hello!</h1>')


class CompanyViewset(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerialzer


class CompanyProfileViewset(ModelViewSet):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer

class AccessibilityViewsets(ModelViewSet):
    queryset = Accessibility.objects.all()
    serializer_class = AccessibilitySerializer


class GuideLinesViewsets(ModelViewSet):
    queryset = GuideLine.objects.all()
    serializer_class = GuideLineSerializer


class CompanyDetailsViewsets(ViewSet):

    def list(self, request):
        queryset = CompanyProfile.objects.all()
        serializer = CompanyDetailsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = CompanyProfile.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = CompanyDetailsSerializer(company)
        return Response(serializer.data)