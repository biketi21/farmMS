from django.urls import path
from logs import views

urlpatterns = [
	path('', views.LogsHome, name='LogsHome'),
	path('BirthLogs/add', views.BirthLogsAdd, name='BirthLogsAdd'),
	path('HarvestLogs/add', views.HarvestLogsAdd, name='HarvestLogsAdd'),
	path('FarmInputLogs/add', views.FarmInputLogsAdd, name='FarmInputLogsAdd'),
	path('MaintenanceLogs/add', views.MaintenanceLogsAdd, name='MaintenanceLogsAdd'),
	path('MedicalLogs/add', views.MedicalLogsAdd, name='MedicalLogsAdd'),
	path('PlantingLogs/add', views.PlantingLogsAdd, name='PlantingLogsAdd'),
	path('<str:log_name>/<int:id>', views.LogsView, name='LogsView'),
]