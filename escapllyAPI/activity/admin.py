from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Activity, ActivityProfile, Difficulty

# Register your models here.

admin.site.register([Activity, ActivityProfile, Difficulty])