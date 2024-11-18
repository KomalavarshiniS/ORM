  # Ex02 Django ORM Web Application
## Date:17.11.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM ##
![Screenshot 2024-11-18 184338](https://github.com/user-attachments/assets/e412ab45-978b-426c-bc16-b1595bd9aee4)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Accountno', 'Amountincome', 'Address')

admin.site.register(Account, AccountAdmin)

models.py

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
```    


## OUTPUT
![alt text](<Screenshot (25).png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
