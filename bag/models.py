from django.db import models

# Create your models here.

class BagAdding(models.Model):

    cosQuantity = models.FloatField(blank=True, null=True)
    cosToken = models.CharField(max_length=70, blank=True)
    number = models.CharField(max_length= 30, blank=True)

class Bagitems(models.Model):
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
    cosToken = models.CharField(max_length=70, blank=True)
    measure = models.CharField(max_length= 30,choices=structure, default=1, blank=False)
    Quantityorder = models.FloatField(blank=True, null=True)
    number = models.CharField(max_length=70, blank=False)

class AddToCart(models.Model):
    structure = (
        ('1', 'normal'),
        ('2', 'Kg'),
        ('3', 'Liter'),
    )
    structure1 = (
        ('Cancelled', 'Cancelled'),
        ('Item Out of Stock', 'Item Out of Stock'),
        ('Order Confirmed', 'Order Confirmed'),
        ('In Processes', 'In Processes'),
        ('Delivered', 'Delivered'),
    )
    cosBrand = models.CharField(max_length=70, blank=False)
    cosName = models.CharField(max_length=70, blank=False)
    cosPrice = models.FloatField(blank=False)
    cosDis = models.FloatField(max_length=30, blank=True, null=True)
    cosQuantity = models.IntegerField(blank=False)
    cosImage1 = models.ImageField(upload_to='', blank=True)
    cosToken = models.CharField(max_length=70, blank=True)
    measure = models.CharField(max_length= 30,choices=structure, default=1, blank=False)
    Quantityorder = models.FloatField(blank=True, null=True)
    number = models.CharField(max_length=70, blank=False)
    order = models.CharField(max_length=30, choices=structure1, default='In Processes', blank=False)
    address = models.CharField(max_length=150, blank=False)

class FullOrder(models.Model):
    fullorder = models.TextField(blank=True)

