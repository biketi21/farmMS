from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from assets.models import *
from .forms import *

# Create your views here.

@login_required(login_url='signin')
def home(request):

	return render(request, "IndexAsset.html")


def ViewAsset(request, asset_name, id):
	asset_name = str.title(asset_name)
	if asset_name == 'Animal':
		asset = get_object_or_404(Animal, id=id)


	

	return render(request, 'assets/view.html', {'asset': asset})

@login_required(login_url='signin')
def AnimalAddAsset(request):
	if request.method == "POST":
		form = AnimalForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Form has been saved.')
	else:
		form = AnimalForm()
		return render(request, 'AddAssets.html', {'form': form})

@login_required(login_url='signin')
def EquipmentAddAsset(request):
	if request.method == "POST":
		form = EquipmentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Form has been saved.')
	else:
		form = EquipmentForm()
		return render(request, 'AddAssets.html', {'form': form})

@login_required(login_url='signin')
def LandAddAsset(request):
	if request.method == "POST":
		form = LandForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Form has been saved.')
	else:
		form = LandForm()
		return render(request, 'AddAssets.html', {'form': form})

@login_required(login_url='signin')
def PlantAddAsset(request):
	if request.method == "POST":
		form = PlantForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Form has been saved.')
	else:
		form = PlantForm()
		return render(request, 'AddAssets.html', {'form': form})

@login_required(login_url='signin')
def SeedAddAsset(request):
	if request.method == "POST":
		form = SeedForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Form has been saved.')
	else:
		form = SeedForm()
		return render(request, 'AddAssets.html', {'form': form})

@login_required(login_url='signin')
def StructureAddAsset(request):
	if request.method == "POST":
		form = StructureForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Form has been saved.')
	else:
		form = StructureForm()
		return render(request, 'AddAssets.html', {'form': form})

		# elif asset_name == "Equipment":
		# 	asset = Equipment.objects.create(
		# 		Farm_ID=request.user,
		# 		Name=request.POST["name"],
		# 		Color=request.POST["color"],
		# 		Manufacturer=request.POST["manufacturer"],
		# 		Serial_No=request.POST["serial"],
		# 		Date_Acquired=request.POST["date_acquired"],
		# 		Notes=request.POST["notes"],
		# 	)
		# elif asset_name == "Land":
		# 	asset = Land.objects.create(
		# 		Farm_ID=request.user,
		# 		Location=request.POST["location"],
		# 		Size_in_Hectares=request.POST["size_in_ha"],
		# 		Type=request.POST["type"],
		# 	)
		# elif asset_name == "Plant":
		# 	asset = Plant.objects.create(
		# 		Farm_ID=request.user,
		# 		Name=request.POST["name"],
		# 		Crop_Variety=request.POST["variety"],
		# 		Plant_Date=request.POST["plant_date"],
		# 		Notes=request.POST["notes"],
		# 	)
		# elif asset_name == "Seed":
		# 	asset = Seed.objects.create(
		# 		Farm_ID=request.user,
		# 		Name=request.POST["name"],
		# 		Crop_Variety=request.POST["variety"],
		# 		Notes=request.POST["notes"],
		# 	)
		# elif asset_name == "Structure":
		# 	asset = Structure.objects.create(
		# 		Farm_ID=request.user,
		# 		Name=request.POST["name"],
		# 		Status=request.POST["status"],
		# 		Type=request.POST["type"],
		# 		Size_in_Feet_Squared=request.POST["size_in_ft"],
		# 	)
	# 	asset.save()
	# 	messages.success(request, "Data Saved to Database.")

	# return render(request, "AddAssets.html")
