from django.db import models

from company.models import Company
# Create your models here.

class Activity(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
