from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Company, CompanyProfile

@receiver(post_save, sender=Company)
def companyprofile_post_save_handler(sender, instance, created, *args, **kwargs):
    if created:
        new_companyprofile = CompanyProfile.objects.create(company=instance)
        new_companyprofile.save()
    else:
        try:
            print(instance.companyprofile)
        except:
            new_companyprofile = CompanyProfile.objects.create(company=instance)
            new_companyprofile.save()
