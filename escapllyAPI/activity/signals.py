from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Activity, ActivityProfile

@receiver(post_save, sender=Activity)
def companyprofile_post_save_handler(sender, instance, created, *args, **kwargs):
    if created:
        new_companyprofile = ActivityProfile.objects.create(activity=instance)
        new_companyprofile.save()
    else:
        try:
            print(instance.activityprofile)
        except:
            new_companyprofile = ActivityProfile.objects.create(activity=instance)
            new_companyprofile.save()