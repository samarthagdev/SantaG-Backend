from django.contrib import admin
from .models import RestroAccount, Categories, Items, Store, PreviousStoreData
# Register your models here.

admin.site.register(RestroAccount)
admin.site.register(Categories)
admin.site.register(Items)
admin.site.register(Store)
admin.site.register(PreviousStoreData)