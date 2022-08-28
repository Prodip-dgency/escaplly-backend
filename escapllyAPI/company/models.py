from django.db import models

from accounts.models import MyUser

# Create your models here.

class Company(models.Model):
    title = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class CompanyProfile(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    address_line = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    website_url = models.CharField(max_length=500, null=True, blank=True)
    about = models.CharField(max_length=1000, null=True, blank=True)
    map_location = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.company)
    
