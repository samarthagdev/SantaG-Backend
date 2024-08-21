from django.contrib import admin
from .models import Cosmaticitems
# Register your models here.
class CosmaticAdmin(admin.ModelAdmin):
    list_display = ('cosBrand', 'cosName')
    search_fields = ('cosBrand', 'cosName')


admin.site.register(Cosmaticitems, CosmaticAdmin)