from django.db import models
from accounts.models import Account

# Create your models here.


SEX_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)

STATUS_CHOICES = (
		('Active', 'Active'),
		('Not_Active', 'Not_Active'),
	)

LAND_TYPE_CHOICES = (
		('Bed', 'Bed'),
		('Field', 'Field'),
		('Paddock', 'Paddock'),
		('Property', 'Property'),
		('Other', 'Other'),
	)

class Animal(models.Model):
	Farm_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
	Name = models.CharField(max_length=20)
	Species = models.CharField(max_length=20)
	Status  = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Active')
	Birth_Date = models.DateTimeField(auto_now_add=True)
	Sex = models.CharField(max_length=10, choices=SEX_CHOICES)
	Tag_ID = models.CharField(unique=True, max_length=10)
	Tag_Location = models.CharField(max_length=20)

	def __str__(self):
		return str(self.Name)

class Equipment(models.Model):
	Farm_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
	Name = models.CharField(max_length=50)
	Color = models.CharField(max_length=20)
	Manufacturer = models.CharField(max_length=30)
	Serial_No  = models.CharField(max_length=20)
	Date_Acquired = models.DateTimeField()
	Notes = models.TextField()

	def __str__(self):
		return str(self.Name)

class Land(models.Model):
	Farm_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
	Location = models.CharField(max_length=50)
	Size_in_Hectares = models.IntegerField()
	Type = models.CharField(max_length=20, choices=LAND_TYPE_CHOICES)

class Plant(models.Model):
	Farm_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
	Name = models.CharField(max_length=20)
	Crop_Variety = models.CharField(max_length=30)
	Plant_Date = models.DateTimeField()
	Notes = models.TextField()

class Seed(models.Model):
	Farm_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
	Name = models.CharField(max_length=20)
	Crop_Variety = models.CharField(max_length=20)
	Notes = models.TextField()

class Structure(models.Model):
	Farm_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
	Name = models.CharField(max_length=30)
	Status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Active')
	Type = models.CharField(max_length=30)
	Size_in_Feet_Squared = models.IntegerField()
