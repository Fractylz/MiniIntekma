from rest_framework import serializers
from .models import Equipment, Plant, Organization, DrivenType, DriverType


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = "__all__"

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"


class DrivenTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrivenType
        fields = "__all__"

class DriverTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverType
        fields = "__all__"