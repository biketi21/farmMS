from django import forms
from .models import *

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields =('__all__')

class EquipmentForm(forms.ModelForm):
	class Meta:
		model = Equipment
		fields = ('__all__')

class LandForm(forms.ModelForm):
	class Meta:
		model = Land
		fields = ('__all__')
class PlantForm(forms.ModelForm):
	class Meta:
		model = Plant
		fields = ('__all__')
class SeedForm(forms.ModelForm):
	class Meta:
		model = Seed
		fields = ('__all__')
class StructureForm(forms.ModelForm):
	class Meta:
		model = Structure
		fields = ('__all__')
