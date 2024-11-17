from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Accountno', 'Amountincome', 'Address')

admin.site.register(Account, AccountAdmin)