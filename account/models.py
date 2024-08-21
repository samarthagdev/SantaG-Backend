from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

# Create your models here.




class AccountManager(BaseUserManager):
    def create_user(self, userName,number,password = None):
        if not userName:
            raise ValueError("Users must have an username")
        if not number:
            raise ValueError("Users must have an number")
        user = self.model(
            userName = userName,
            number = number,

        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, userName,number,password):
        user = self.create_user(
            userName=userName,
            password=password,
            number=number
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class Account(AbstractBaseUser):
    userName = models.CharField(max_length=70, blank=False)
    number = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to='media/userimage',default='media/userimage/hi.png')
    date_joined = models.DateTimeField(verbose_name='date-joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last-joined', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD ='number'
    REQUIRED_FIELDS = ['userName']

    objects = AccountManager()

    def __str__(self):
        return self.userName

    def has_perm(self,perm, obj=None):
        return  self.is_admin

    def has_module_perms(self,app_label):
        return True



