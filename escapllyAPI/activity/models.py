from django.db import models

from company.models import Company

# Create your models here.

class Activity(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'activities'
    
    def __str__(self):
        return self.title


class Difficulty(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'difficulties'

    def __str__(self):
        return self.title


class ActivityProfile(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=150, null=True, blank=True)
    website_link = models.CharField(max_length=200, null=True, blank=True)
    storyline = models.CharField(max_length=1000, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    minimum_participant = models.IntegerField(null=True, blank=True)
    maximum_participant =  models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.SET_NULL, null=True, blank=True)
    mimimum_age = models.IntegerField(null=True, blank=True)
    accompany_age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    main_image = models.ForeignKey('gallery.GalleryItem', related_name='activity_main_image', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.activity)
    