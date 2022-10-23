from django.db import models

from accounts.models import MyUser
# from activity.models import Activity

# Create your models here.

class Company(models.Model):
    title = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.title


class Accessibility(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'accessibilities'

    def __str__(self):
        return self.title


class GuideLine(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title



class CompanyProfile(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    address_line = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    website_url = models.CharField(max_length=500, null=True, blank=True)
    about = models.CharField(max_length=1000, null=True, blank=True)
    map_location = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    profile_image = models.ForeignKey('gallery.GalleryItem', on_delete=models.SET_NULL, related_name='profile_image', null=True, blank=True)
    cover_image = models.ForeignKey('gallery.GalleryItem', on_delete=models.SET_NULL, related_name='cover_image', null=True, blank=True)
    accessibility = models.ManyToManyField(Accessibility, blank=True)
    guideline = models.ManyToManyField(GuideLine, blank=True)


    def getActivities(self):
        owncompany = self.company
        activities = owncompany.activity_set.all()
        total_activities = len(activities)
        return {"activities": activities, "total_activities":total_activities}

    def __str__(self):
        return str(self.company)
    
