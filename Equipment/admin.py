from django.contrib import admin
from .models import Equipment, Plant, Organization, DriverType, DrivenType


admin.site.register(Organization)

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'client')

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("tag", "plant", "driver_type", "driven_type")

@admin.register(DriverType)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(DrivenType)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("name",)