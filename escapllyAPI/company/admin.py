from django.contrib import admin

from .models import Company, CompanyProfile, Accessibility, GuideLine

# Register your models here.

admin.site.register([Company, CompanyProfile, Accessibility, GuideLine])
