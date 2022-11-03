from django.db import models
from django.utils import timezone

# Create your models here.

class ContactForm1(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_no = models.CharField(max_length=20)
    subject_of_communication = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    message = models.TextField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=timezone.now)

    class Meta:
        verbose_name = 'Contact Form(1) submission'
        verbose_name_plural = 'Contact Form(1) submissions'

    def __str__(self):
        return '{}____{}____{}'.format(self.first_name, self.email, self.subject_of_communication)