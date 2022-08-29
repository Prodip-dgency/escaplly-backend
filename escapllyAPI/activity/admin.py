from atexit import register
import site
from django.contrib import admin

from .models import Activity, ActivityProfile

# Register your models here.

admin.site.register([Activity, ActivityProfile])


