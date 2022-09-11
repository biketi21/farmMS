from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from logs.models import *
from .forms import *

# Create your views here.
@login_required(login_url='signin')
def LogsHome(request):
	return render(request, 'IndexLogs.html')


@login_required(login_url='signin')
def LogsView(request, log_name, id):
    log_name = str.title(log_name)
    log = get_object_or_404(log_name, id=id)

    return render(request, 'logs/view.html', {'logs': logs})



@login_required(login_url='signin')
def BirthLogsAdd(request):
	if request.method == "POST":
		form = BirthForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Form has been saved.')
	else:
		form = BirthLogsForm()
		return render(request, 'AddAssets.html', {'form': form})

@login_required(login_url='signin')
def HarvestLogsAdd(request):
	if request.method == "POST":
		form = HarvestForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Form has been saved.')
	else:
		form = HarvestForm()
		return render(request, 'AddAssets.html', {'form': form})

@login_required(login_url='signin')
def FarmInputLogsAdd(request):
	if request.method == "POST":
		form = FarmInputForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Form has been saved.')
	else:
		form = FarmInputForm()
		return render(request, 'AddAssets.html', {'form': form})

@login_required(login_url='signin')
def MaintenanceLogsAdd(request):
	if request.method == "POST":
		form = MaintenanceForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Form has been saved.')
	else:
		form = MaintenanceForm()
		return render(request, 'AddAssets.html', {'form': form})

@login_required(login_url='signin')
def MedicalLogsAdd(request):
	if request.method == "POST":
		form = MedicalForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Form has been saved.')
	else:
		form = MedicalForm()
		return render(request, 'AddAssets.html', {'form': form})

@login_required(login_url='signin')
def PlantingLogsAdd(request):
	if request.method == "POST":
		form = PlantingForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Form has been saved.')
	else:
		form = PlantingForm()
		return render(request, 'AddAssets.html', {'form': form})
































# def LogsAdd(request, log_name):
# 	log_name = str.title(log_name)
# 	if request.method == 'POST':
# 		if log_name == 'Birth_Logs':
# 			logs = Birth_Logs.objects.create(
# 				Farm_ID = request.user,
# 				Date = request.POST['date'],
# 				Veterinarian = request.POST['vet'],
# 				Mother_by_TagID = request.POST['mother'],
# 				Species =request.POST['species'],
# 				Equipment_Used = request.POST['equipment'],
# 				Notes = request.POST['notes'],
# 			)
# 		elif log_name == 'Harvest_Logs':
# 			logs = Harvest_Logs.objects.create(
# 				Farm_ID = request.user,
# 				Log_Name = request.POST['log_name'],
# 				Date = request.POST['date'],
# 				Asset = request.POST['asset'],
# 				Location = request.POST['location'],
# 				Equipment_Used = request.POST['equipment'],
# 				Quantity = request.POST['quantity'],
# 				Storage_ID = request.POST['storage'],
# 			)
# 		elif log_name == 'Farm_Input_Logs':
# 			logs = Farm_Input_Logs.objects.create(
# 				Farm_ID = request.user,
# 				Log_Name = request.POST['log_name'],
# 				Location = request.POST['location'],
# 				Material_Type = request.POST['type'],
# 				Source = request.POST['source'],
# 				Quantity = request.POST['quantity'],
# 			)
# 		elif log_name == 'Maintenance_Logs':
# 			logs = Maintenance_Logs.objects.create(
# 				Farm_ID = request.user,
# 				Asset = request.POST['asset'],
# 				Equipment_Used = request.POST['equipment'],
# 				Date = request.POST['date'],
# 			)
# 		elif log_name == 'Medical_Logs':
# 			logs = Medical_Logs.objects.create(
# 				Farm_ID = request.user,
# 				Log_Name = request.POST['log_name'],
# 				Asset_Affected = request.POST['asset'],
# 				Location = request.POST['location'],
# 				Veterinarian = request.POST['vet'],
# 			)
# 		elif log_name == 'Planting_Logs':
# 			logs = Planting_Logs.objects.create(
# 				Farm_ID = request.user,
# 				Season = request.POST['season'],
# 				Crop_Variety = request.POST['variety'],
# 				Number_of_Varieties = request.POST['no_of_variety'],
# 				Date = request.POST['date'],
# 				Inputs = request.POST['inputs'],
# 			)

# 		logs.save()
# 		messages.success(request, 'Log Saved to Database.')

# 	return render(request, 'AddLogs.html')