from django.db import models

# Create your models here.
class HotelName(models.Model):

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class MenuCard(models.Model):
    post = models.ForeignKey(HotelName,to_field='name', on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='media/menu/')