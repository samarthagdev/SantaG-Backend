from django.db import models

# Create your models here.
class OfferPoster(models.Model):
    img = models.ImageField(upload_to='media/offerposter/', blank=True)
    url = models.CharField(max_length=40, blank=True)
    name = models.CharField(max_length=300, blank=True)

class OfferPoster1(models.Model):
    img = models.ImageField(upload_to='media/offerposter1/', blank=True)
    url = models.CharField(max_length=300, blank=True)
    name = models.CharField(max_length=300, blank=True)
class OfferPoster2(models.Model):
    img = models.ImageField(upload_to='media/offerposter2/', blank=True)
    url = models.CharField(max_length=40, blank=True)
    name = models.CharField(max_length=40, blank=True)

class OfferPoster3(models.Model):
    img = models.ImageField(upload_to='media/offerposter3/', blank=True)
    url = models.CharField(max_length=40, blank=True)
    name = models.CharField(max_length=300, blank=True)
