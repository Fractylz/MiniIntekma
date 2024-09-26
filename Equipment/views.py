from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Equipment, Organization, Plant, DriverType, DrivenType
from .serializers import EquipmentSerializer, OrganizationSerializer, PlantSerializer, DrivenTypeSerializer, DriverTypeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
 

class EquipmentList(APIView):
    def get(self, request, format=None):
        equipments = Equipment.objects.all()
        serializer = EquipmentSerializer(equipments, many=True)  
        return Response(serializer.data)

class EquipmentDetail(APIView):
    def get(self, request, id, format=None):
        equipment = Equipment.objects.get(id=id)
        serializer = EquipmentSerializer(equipment)  
        return Response(serializer.data)  

class OrganizationList(APIView):
    def get(self, request, format=None):
        organizations = Organization.objects.all()  
        serializer = OrganizationSerializer(organizations, many=True)  
        return Response(serializer.data)  

class PlantList(APIView):
    def get(self, request, format=None):
        plants = Plant.objects.all()  
        serializer = PlantSerializer(plants, many=True)  
        return Response(serializer.data)
    
class DriverTypeList(APIView):
    def get(self, request, format=None):
        driver_type = DriverType.objects.all()  
        serializer = DriverTypeSerializer(driver_type, many=True)  
        return Response(serializer.data)
    
class DrivenTypeList(APIView):
    def get(self, request, format=None):
        driven_type = DrivenType.objects.all()  
        serializer = DrivenTypeSerializer(driven_type, many=True)  
        return Response(serializer.data)
    
