from django import forms
from .models import *

class BirthForm(forms.ModelForm):
    class Meta:
        model = Birth_Logs
        fields =('__all__')

class HarvestForm(forms.ModelForm):
	class Meta:
		model = Harvest_Logs
		fields = ('__all__')

class FarmInputForm(forms.ModelForm):
	class Meta:
		model = Farm_Input_Logs
		fields = ('__all__')
class MaintenanceForm(forms.ModelForm):
	class Meta:
		model = Maintenance_Logs
		fields = ('__all__')
class MedicalForm(forms.ModelForm):
	class Meta:
		model = Medical_Logs
		fields = ('__all__')
class PlantingForm(forms.ModelForm):
	class Meta:
		model = Planting_Logs
		fields = ('__all__')
