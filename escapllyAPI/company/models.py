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
        activity_profiles = []
        lowest_age = None
        average_minimum_participant = None
        average_maximum_participant = None
        highest_accompany_age = None
        average_game_duration = None
        for item in activities:
            activity_profiles.append(item.activityprofile)
        if activity_profiles:
            lowest_age = activity_profiles[0].mimimum_age
            average_minimum_participant = activity_profiles[0].minimum_participant
            average_maximum_participant = activity_profiles[0].maximum_participant
            highest_accompany_age = activity_profiles[0].accompany_age
            game_duration = activity_profiles[0].duration
            for activity_profile in activity_profiles:
                game_duration = activity_profile.duration + game_duration
                if activity_profile.mimimum_age < lowest_age:
                    lowest_age = activity_profile.mimimum_age
                if activity_profile.minimum_participant < average_minimum_participant:
                    average_minimum_participant = activity_profile.minimum_participant
                if activity_profile.maximum_participant > average_maximum_participant:
                    average_maximum_participant = activity_profile.maximum_participant
                if activity_profile.accompany_age > highest_accompany_age:
                    highest_accompany_age = activity_profile.accompany_age

            if game_duration:
                average_game_duration = round(game_duration/len(activity_profiles), 0)        

        total_activities = len(activities)


        values = {
            "activitie_profiles": activity_profiles,
            "total_activities":total_activities,
            'lowest_age': lowest_age,
            'average_minimum_participant': average_minimum_participant,
            'average_maximum_participant': average_maximum_participant,
            'highest_accompany_age': highest_accompany_age,
            'average_game_duration': average_game_duration
        }

        return values


    def getAllRelatedGalleryItems(self):
        own_company = self.company
        own_gallery_items = own_company.galleryitem_set.all()
        return own_gallery_items

    def __str__(self):
        return str(self.company)
    
