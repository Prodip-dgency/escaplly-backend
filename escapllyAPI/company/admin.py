from django.contrib import admin

from .models import Company, CompanyProfile, Accessibility

# Register your models here.

admin.site.register([Company, CompanyProfile, Accessibility])
