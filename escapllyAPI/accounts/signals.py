from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import MyUser, UserProfile

@receiver(post_save, sender=MyUser)
def myuser_post_save_handler(sender, instance, created, *args, **kwargs):
    if created:
        new_userprofile = UserProfile.objects.create(user=instance)
        new_userprofile.save()
    else:
        try:
            print(instance.userprofile)
        except:
            new_userprofile = UserProfile.objects.create(user=instance)
            new_userprofile.save()