from django.contrib import admin
from .models import BagAdding, Bagitems,AddToCart, FullOrder

class BagAdmin(admin.ModelAdmin):
    list_display = ('cosBrand', 'cosName')



# Register your models here.

admin.site.register(BagAdding)
admin.site.register(FullOrder)
admin.site.register(Bagitems)
admin.site.register(AddToCart, BagAdmin)