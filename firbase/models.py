from django.db import models

# Create your models here.

class devicetoken(models.Model):

    fcm_token = models.CharField(max_length=400, blank=False,null=False)
    number = models.CharField(max_length=30, unique=True)