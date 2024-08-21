from django.contrib import admin
from .models import Account
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('userName', 'number')
    search_fields = ('userName', 'number')

admin.site.register(Account, AccountAdmin)
