from django.shortcuts import render
from rest_framework import Permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.views import APIView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import  Customer, Crop, Land, Season, Labourer, Equipment, Equipment_Vendor, Seed, Seeds_Vendor, Pesticides, Pesticides_Vendor, Inorganic_Fertilizers, Inorganic_Fertlizer_Vendor, Organic_Fertilizers, Organic_Fertlizer_Vendor,  Soil_Test, Equipment_Mapping, Organic_Fertilizers_Mapping, Inorganic_Fertilizers_Mapping, Pesticides_Mapping, Seeds_Mapping, Season_Mapping, Potential_Market, Equipment_Available, Inorganic_Fertilizers_Available, Organic_Fertilizers_Available, Pesticides_Available, Seeds_Available
from .serializers import CustomerSerializer, CropSerializer, LandSerializer, SeasonSerializer, LabourerSerializer, EquipmentSerializer, Equipment_VendorSerializer, SeedSerializer, Seeds_VendorSerializer, PesticidesSerializer, Pesticides_VendorSerializer, Inorganic_FertilizersSerializer, Inorganic_Fertlizer_VendorSerializer, Organic_FertilizersSerializer, Organic_Fertlizer_VendorSerializer,  Soil_TestSerializer, Equipment_MappingSerializer, Organic_Fertilizers_MappingSerializer, Inorganic_Fertilizers_MappingSerializer, Pesticides_MappingSerializer, Seeds_MappingSerializer, Season_MappingSerializer, Potential_MarketSerializer, Equipment_AvailableSerializer, Inorganic_Fertilizers_AvailableSerializer, Organic_Fertilizers_AvailableSerializer, Pesticides_AvailableSerializer, Seeds_AvailableSerializer

class API_Customer(APIView):
    def get(self, request):
        Customer = customer.objects.all().order_by('id')
        serializer = CustomerSerializer(Customer, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class API_Crop(APIView):
    def get(self, request):
        Crop = crop.objects.all().order_by('id')
        serializer = CropSerializer(Crop, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = CropSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Land(APIView):
    def get(self, request):
        Land = land.objects.all().order_by('id')
        serializer = LandSerializer(Land, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = LandSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Season(APIView):
    def get(self, request):
        Season = season.objects.all().order_by('id')
        serializer = SeasonSerializer(Season, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = SeasonSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Labourer(APIView):
    def get(self, request):
        Labourer = labourer.objects.all().order_by('id')
        serializer = LabourerSerializer(Labourer, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = LabourerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Equipment(APIView):
    def get(self, request):
        Equipment = equipment.objects.all().order_by('id')
        serializer = EquipmentSerializer(Equipment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = EquipmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Equipment_Vendor(APIView):
    def get(self, request):
        Equipment_Vendor = equipment_vendor.objects.all().order_by('id')
        serializer = Equipment_VendorSerializer(Equipment_Vendor, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Equipment_VendorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)