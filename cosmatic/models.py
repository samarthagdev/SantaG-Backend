from django.db import models

# Create your models here.

class Cosmaticitems(models.Model):
    structure = (
        ('1', 'normal'),
        ('2', 'Kg'),
        ('3', 'Liter'),
    )
    cosBrand = models.CharField(max_length=70, blank=False)
    cosName = models.CharField(max_length=70, blank=False)
    cosPrice = models.FloatField(blank=False)
    cosDis = models.FloatField(max_length=30, blank=True, null=True)
    cosQuantity = models.IntegerField(blank=False)
    cosImage1 = models.ImageField(upload_to='media/cosmaticimages/', blank=True)
    cosImage2 = models.ImageField(upload_to='media/cosmaticimages/', blank=True)
    cosImage3 = models.ImageField(upload_to='media/cosmaticimages/', blank=True)
    cosImage4 = models.ImageField(upload_to='media/cosmaticimages/', blank=True)
    cosToken = models.CharField(max_length=70, blank=True)
    measure = models.CharField(max_length= 30,choices=structure, default=1, blank=False)
    measure1 = models.CharField(max_length=150, blank=True)
    maxlimit = models.CharField(max_length=150, blank=True)
    minlimit = models.CharField(max_length=150, blank=True)
    specialuri = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True,default='No Description Available for this product')




