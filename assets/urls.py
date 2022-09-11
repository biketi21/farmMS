from django.urls import path
from assets import views

urlpatterns = [
	path('', views.home, name='assetshome'),
	path('<str:asset_name>/<int:id>', views.ViewAsset, name='ViewAsset'),
	path('Animal/add', views.AnimalAddAsset, name='AnimalAddAsset'),
	path('Equipment/add', views.EquipmentAddAsset, name='EquipmentAddAsset'),
	path('Land/add', views.LandAddAsset, name='LandAddAsset'),
	path('Plant/add', views.PlantAddAsset, name='PlantAddAsset'),
	path('Seed/add', views.SeedAddAsset, name='SeedAddAsset'),
	path('Structure/add', views.StructureAddAsset, name='StructureAddAsset'),
]