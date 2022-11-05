from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import GalleryItem


@receiver(post_delete, sender=GalleryItem)
def GalleryItemDelete(sender, instance, *args, **kwargs):
    if instance.image:
        instance.image.delete(False)
