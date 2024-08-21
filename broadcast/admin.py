from django.contrib import admin
from .models import Otpveification, Otpveification1, Version
# Register your models here.

admin.site.register(Version)
admin.site.register(Otpveification)
admin.site.register(Otpveification1)