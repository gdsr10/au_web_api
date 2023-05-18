from django.contrib import admin
from backend import models

# Register your models here.

admin.site.register(models.UserAccount)
admin.site.register(models.MedicalCenterMaster)
admin.site.register(models.EntryDetails)