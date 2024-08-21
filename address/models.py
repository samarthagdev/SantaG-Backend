from django.db import models

# Create your models here.

class Address(models.Model):
    address = models.CharField(max_length=150, blank=False)
    number = models.CharField(max_length=70, blank=False)