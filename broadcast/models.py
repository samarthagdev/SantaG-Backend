from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Version(models.Model):
    version = models.CharField(max_length=20, blank=False)

class Otpveification(models.Model):
    userName = models.CharField(max_length=70, blank=False)
    password = models.CharField(max_length=70, blank=False)
    number = models.CharField(max_length=30, blank=True, null=True)
    otp = models.IntegerField(blank=True, default=0)
    number_trial = models.IntegerField(blank=True, default=0)
    timestamps = models.TimeField(auto_now_add=True)

class Otpveification1(models.Model):
    number = models.CharField(max_length=30, blank=True, null=True)
    otp = models.IntegerField(blank=True, default=0)
    number_trial = models.IntegerField(blank=True, default=0)
    timestamps = models.TimeField(auto_now_add=True)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)