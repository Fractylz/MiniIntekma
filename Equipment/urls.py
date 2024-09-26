from django.urls import path
from .views import EquipmentList, EquipmentDetail, OrganizationList, PlantList, DriverTypeList, DrivenTypeList

urlpatterns = [
    path('api/equipments/', EquipmentList.as_view(), name='equipment-list'),
    path('api/equipments/<int:id>/', EquipmentDetail.as_view(), name='equipment-detail'),
    path('api/organizations/', OrganizationList.as_view(), name='organization-list'),
    path('api/plants/', PlantList.as_view(), name='plant-list'),
    path('api/driverType/', DriverTypeList.as_view(), name='driverType-list'),
    path('api/drivenType/', DrivenTypeList.as_view(), name='drivenType-list'),
    
]

