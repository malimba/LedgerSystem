from django.db import models

# Create your models here.
class Service(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    serviceName = models.CharField(max_length=21, blank=False, null=False)
    serviceCode = models.CharField(max_length=15, blank=False, null=False)#this is the specific code recognizable by expressPay

class BankDetails(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    bankName = models.CharField(max_length=50, blank=False, null=False)
    sortCode = models.IntegerField(blank=False, null=False)

class PackageDetails(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    packageName = models.CharField(max_length=25, blank=False, null=False)
    packageAmount = models.IntegerField(blank=False, null=False)
    packageDesc = models.TextField(blank=False, null=False, default='PACKAGE DETAILS GO HERE')



