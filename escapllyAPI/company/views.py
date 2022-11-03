from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response


from .models import Company, CompanyProfile, Accessibility, GuideLine
from .serializers import (CompanyProfileSafeSerializer, CompanySafeSerializer, CompanySerializer, 
                          CompanyProfileSerializer, AccessibilitySerializer, 
                          CompanyDetailsSerializer, GuideLineSerializer)


def CompanyHome(request):
    return HttpResponse('<h1>Hello!</h1>')


class CompanyViewset(ModelViewSet):
    queryset = Company.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return CompanySafeSerializer
        return CompanySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()

        if self.request.method in SAFE_METHODS:
            context['exclude_fields'] = {
                                            'MyUser': {
                                                'password', 
                                                'last_login', 
                                                'is_superuser', 
                                                'is_staff', 
                                                'is_active', 
                                                'date_joined', 
                                                'groups', 
                                                'user_permissions'
                                            },
                                        }
        return context
        

class CompanyProfileViewset(ModelViewSet):
    queryset = CompanyProfile.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return CompanyProfileSafeSerializer
        return CompanyProfileSerializer


class AccessibilityViewsets(ModelViewSet):
    queryset = Accessibility.objects.all()
    serializer_class = AccessibilitySerializer


class GuideLinesViewsets(ModelViewSet):
    queryset = GuideLine.objects.all()
    serializer_class = GuideLineSerializer


class CompanyDetailsViewsets(ViewSet):

    def list(self, request):
        queryset = CompanyProfile.objects.all()
        context = {
            'request': request,
            'exclude_fields': {
                'GalleryItem': {
                    'id',
                    'title',
                    'description',
                    'user',
                    'company',
                    'activity'
                }
            }
        }
        print(repr(self))
        

        serializer = CompanyDetailsSerializer(queryset, many=True, context=context)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = CompanyProfile.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = CompanyDetailsSerializer(company)
        return Response(serializer.data)