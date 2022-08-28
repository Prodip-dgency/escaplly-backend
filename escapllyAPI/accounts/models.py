from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db import models

# Create your models here.
class MyUser(AbstractUser):
    username = models.CharField(_('username'), max_length=50, null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return('{}, {}'.format(self.email, self.id))


class UserProfile(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    