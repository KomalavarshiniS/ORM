from django.db import models
from django.contrib import admin

class Account(models.Model):
    Name = models.CharField(max_length=100)  
    Accountno = models.IntegerField(primary_key=True)  
    Amountincome = models.FloatField()
    Address = models.CharField(max_length=255) 

    def _str_(self):
        return f"Account {self.Accountno} - {self.Name}"

class AccountAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Accountno', 'Amountincome','Address')