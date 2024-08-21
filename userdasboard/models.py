from django.db import models

# Create your models here.

class Userdasboard(models.Model):
    structure = (
        ('1', 'None'),
        ('2', 'structure1'),
        ('3', 'structure2'),
        ('4', 'structure3'),
        ('5', 'structure4'),
        ('6', 'structure5'),
        ('7', 'structure6'),
        ('8', 'structure7'),
        ('9', 'structure8')

    )
    itemname = models.ImageField(upload_to='media/userdasboardtitle/', blank=True)
    switch = models.BooleanField(default=False)
    identity = models.CharField(max_length=30, blank=False, choices= structure)
    url = models.CharField(max_length=150,blank= True )