from django.db import models

# Create your models here.


class RestroAccount(models.Model):
    userName = models.CharField(max_length=70, blank=False,)
    number = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=200, blank=False)
    tk = models.CharField(max_length=70, unique=True, blank=True)
    firebasetk = models.CharField(max_length=500,blank=True)
    image = models.ImageField(upload_to='media/userimage', default='media/userimage/hi.png')
    date_joined = models.DateTimeField(verbose_name='date-joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last-joined', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    unique_tag = models.CharField(max_length=70, blank=True)


class Categories(models.Model):
    category = models.CharField(max_length=150, blank=False,)


class Items(models.Model):
    category_items = models.CharField(max_length=150, blank=False,)
    items = models.CharField(max_length=150, blank=False,)
    price = models.FloatField(max_length=150, blank=False,)

# storing data for web Socket


class Store(models.Model):
    uni_name = models.CharField(max_length=200)
    msg = models.CharField(max_length=10000)
    table_no = models.CharField(max_length=100, blank=False)


class PreviousStoreData(models.Model):
    uni_name = models.CharField(max_length=200)
    table_data = models.CharField(max_length=10000)
    table_no = models.CharField(max_length=100, blank=False)
    order_taker = models.CharField(max_length=100, blank=False)
    net_amount = models.FloatField()
    time = models.CharField(max_length=150)
    position = models.CharField(max_length=70,default='finalize')