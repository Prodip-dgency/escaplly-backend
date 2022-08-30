from django.db import models
from django.contrib.auth import get_user_model

from company.models import Company

# Create your models here.

User = get_user_model()

class GalleryItem(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='gallery/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{}-{}".format(self.title, self.user)
    