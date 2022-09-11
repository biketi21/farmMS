from django.db import models
from assets.models import Animal, Equipment
from accounts.models import Account

class Birth_Logs(models.Model):
	Farm_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
	Date = models.DateTimeField()
	Veterinarian = models.CharField(max_length=30)
	Mother_by_TagID = models.ForeignKey(Animal, on_delete=models.CASCADE)
	Species = models.CharField(max_length=20)
	Equipment_Used = models.CharField(max_length=100)
	Notes = models.TextField()

class Harvest_Logs(models.Model):
	Farm_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
	Log_Name = models.CharField(max_length=20)
	Date     = models.DateTimeField()
	Asset    = models.CharField(max_length=20)
	Location = models.CharField(max_length=20)
	Equipment_Used = models.CharField(max_length=100)
	Quantity = models.CharField(max_length=20)
	Storage_ID = models.CharField(max_length=5)

class Farm_Input_Logs(models.Model):
	Farm_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
	Log_Name = models.CharField(max_length=20)
	Location = models.CharField(max_length=20)
	Material_Type = models.CharField(max_length=20)
	Source = models.CharField(max_length=20)
	Quantity = models.CharField(max_length=20)

class Maintenance_Logs(models.Model):
	Farm_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
	Asset = models.CharField(max_length=20)
	Equipment_Used = models.CharField(max_length=100)
	Date = models.DateTimeField()

class Medical_Logs(models.Model):
	Farm_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
	Log_Name = models.CharField(max_length=20)
	Asset_Affected = models.CharField(max_length=20)
	Location = models.CharField(max_length=20)
	Veterinarian = models.CharField(max_length=30)

class Planting_Logs(models.Model):
	Farm_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
	Season = models.CharField(max_length=20)
	Crop_Variety = models.CharField(max_length=20)
	Number_of_Varieties = models.IntegerField()
	Date = models.DateTimeField()
	Inputs = models.CharField(max_length=20)

