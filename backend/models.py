from django.db import models

# Create your models here.

class UserAccount(models.Model):
    """UserAccount table
    """
    UserCode = models.PositiveIntegerField(primary_key=True)
    UserName = models.CharField(max_length=100, default='',blank= True)
    FullName = models.CharField(max_length=50, default='',blank= True)
    ContactNo = models.CharField(max_length=20, default='',blank= True)
    EmailId = models.CharField(max_length=100, default='',null=True, blank=True)
    UserPass = models.CharField(max_length=100, null=True, blank=True)
    UserType = models.CharField(max_length=50, default='', blank=True)
    UserTypeName = models.CharField(max_length=50, default='', blank=True)
    Status = models.CharField(max_length=1, default='A')
    

class MedicalCenterMaster(models.Model):
    """MedicalCenterMaster table
    """
    MedicalCenterCode = models.PositiveIntegerField(primary_key=True)
    MedicalCenterName = models.CharField(max_length=100, default='', null=True, blank=True)
    MedicalCenterTypeCode = models.IntegerField(default='', null=True, blank=True)
    Status = models.CharField(max_length=1, default='A')
    
    
class EntryDetails(models.Model):
    """EntryDetails table
    """
    EntryDetailsCode = models.PositiveIntegerField(primary_key=True)
    UserCode = models.ForeignKey(UserAccount, on_delete=models.PROTECT)
    MedicalCenterCode = models.ForeignKey(MedicalCenterMaster, on_delete=models.PROTECT)
    EntryDate = models.DateField(blank=True, null=True)
    Status = models.CharField(max_length=1, default='A')