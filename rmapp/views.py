from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.views import APIView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView 
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomerForm
from django.contrib.auth.models import User       
from .models import Customer
from .filters import CustomerFilterSet
from bootstrap_modal_forms.generic import (BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView) 
from django.contrib import messages
from django_filters.views import BaseFilterView
from .models import  Customer, Crop, Land, Season, Labourer, Equipment, Equipment_Vendor, Seed, Seeds_Vendor, Pesticides, Pesticides_Vendor, Inorganic_Fertilizers, Inorganic_Fertlizer_Vendor, Organic_Fertilizers, Organic_Fertlizer_Vendor,  Soil_Test, Equipment_Mapping, Organic_Fertilizers_Mapping, Inorganic_Fertilizers_Mapping, Pesticides_Mapping, Seeds_Mapping, Season_Mapping, Potential_Market, Equipment_Available, Inorganic_Fertilizers_Available, Organic_Fertilizers_Available, Pesticides_Available, Seeds_Available
from .serializers import CustomerSerializer, CropSerializer, LandSerializer, SeasonSerializer, LabourerSerializer, EquipmentSerializer, Equipment_VendorSerializer, SeedSerializer, Seeds_VendorSerializer, PesticidesSerializer, Pesticides_VendorSerializer, Inorganic_FertilizersSerializer, Inorganic_Fertlizer_VendorSerializer, Organic_FertilizersSerializer, Organic_Fertlizer_VendorSerializer,  Soil_TestSerializer, Equipment_MappingSerializer, Organic_Fertilizers_MappingSerializer, Inorganic_Fertilizers_MappingSerializer, Pesticides_MappingSerializer, Seeds_MappingSerializer, Season_MappingSerializer, Potential_MarketSerializer, Equipment_AvailableSerializer, Inorganic_Fertilizers_AvailableSerializer, Organic_Fertilizers_AvailableSerializer, Pesticides_AvailableSerializer, Seeds_AvailableSerializer

class CustomerListView(BaseFilterView,ListView):
    template_name="rmapp/customer.html"
    model=Customer
    paginate_by=25
    context_object_name='Customer'
    filterset_class=CustomerFilterSet

class CustomerCreateView (BSModalCreateView):
    template_name="rmapp/add_profile.html"
    form_class=CustomerForm
    success_message='Success:Customer Details were updated'
    success_url=reverse_lazy('Customer_list')

class CustomerUpdateView(BSModalUpdateView):
    model=Customer
    template_name='rmapp/update_profile.html'
    form_class=CustomerForm
    success_message='Success:Customer Details were updated'
    success_url=reverse_lazy('Customer_list')

class API_Customer(APIView):
    def get(self, request):
        Customers = Customer.objects.all().order_by('id')
        serializer = CustomerSerializer(Customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def customer_detail(request,pk):
    try:
        Customers = Customer.objects.get(pk=pk)
    except Customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSeralizer(Customers)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(Customers,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class API_Crop(APIView):
    def get(self, request):
        Crops = Crop.objects.all().order_by('id')
        serializer = CropSerializer(Crops, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = CropSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Crop_detail(request,pk):
    try:
        Crops = Crop.objects.get(pk=pk)
    except Crops.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CropSerializer(Crops)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CropSerializer(Crops,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class API_Land(APIView):
    def get(self, request):
        Lands = Land.objects.all().order_by('id')
        serializer = LandSerializer(Lands, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = LandSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Land_detail(request,pk):
    try:
        Lands = Land.objects.get(pk=pk)
    except Lands.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LandSerializer(Lands)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LandSerializer(Lands,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Season(APIView):
    def get(self, request):
        Seasons = Season.objects.all().order_by('id')
        serializer = SeasonSerializer(Seasons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = SeasonSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Season_detail(request,pk):
    try:
        Seasons = Season.objects.get(pk=pk)
    except Seasons.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SeasonSerializer(Seasons)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SeasonSerializer(Seasons,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Labourer(APIView):
    def get(self, request):
        Labourers = Labourer.objects.all().order_by('id')
        serializer = LabourerSerializer(Labourers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = LabourerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Labourer_detail(request,pk):
    try:
        Labourers = Labourer.objects.get(pk=pk)
    except Labourers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LabourerSerializer(Labourers)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LabourerSerializer(Labourers,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Equipment(APIView):
    def get(self, request):
        Equipments = Equipment.objects.all().order_by('id')
        serializer = EquipmentSerializer(Equipments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = EquipmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Equipment_detail(request,pk):
    try:
        Equipments = Equipment.objects.get(pk=pk)
    except Equipments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EquipmentSerializer(Equipments)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EquipmentSerializer(Equipments,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Equipment_Vendor(APIView):
    def get(self, request):
        Equipment_Vendors = Equipment_Vendor.objects.all().order_by('id')
        serializer = Equipment_VendorSerializer(Equipment_Vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Equipment_VendorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Equipment_Vendor_detail(request,pk):
    try:
        Equipment_Vendors = Equipment_Vendor.objects.get(pk=pk)
    except Equipment_Vendors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Equipment_VendorSerializer(Equipment_Vendors)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Equipment_VendorSerializer(Equipment_Vendors,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Seed(APIView):
    def get(self, request):
        Seeds = Seed.objects.all().order_by('id')
        serializer = SeedSerializer(Seeds, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = SeedSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Seed_detail(request,pk):
    try:
        Seeds = Seed.objects.get(pk=pk)
    except Seeds.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SeedSerializer(Seeds)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SeedSerializer(Seeds,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Seeds_Vendor(APIView):
    def get(self, request):
        Seeds_Vendor = seeds_vendor.objects.all().order_by('id')
        serializer = Seeds_VendorSerializer(Seeds_Vendor, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Seeds_VendorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Seeds_Vendor_detail(request,pk):
    try:
        Seeds_Vendor = seeds_vendor.objects.get(pk=pk)
    except seeds_vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Seeds_VendorSerializer(Seeds_Vendor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Seeds_VendorSerializer(Seeds_Vendor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Pesticides(APIView):
    def get(self, request):
        Pesticides = Pesticide.objects.all().order_by('id')
        serializer = PesticidesSerializer(Pesticides, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = PesticidesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Pesticides_detail(request,pk):
    try:
        Pesticides = Pesticide.objects.get(pk=pk)
    except Pesticides.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PesticidesSerializer(Pesticides)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PesticidesSerializer(Pesticides,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Pesticides_Vendor(APIView):
    def get(self, request):
        Pesticides_Vendors = Pesticides_Vendor.objects.all().order_by('id')
        serializer = Pesticides_VendorSerializer(Pesticides_Vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Pesticides_VendorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Pesticides_Vendor_detail(request,pk):
    try:
        Pesticides_Vendors = Pesticides_Vendor.objects.get(pk=pk)
    except Pesticides_Vendors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Pesticides_VendorSerializer(Pesticides_Vendors)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Pesticides_VendorSerializer(Pesticides_Vendors,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Inorganic_Fertilizers(APIView):
    def get(self, request):
        Inorganic_Fertilizers = Inorganic_Fertilizers.objects.all().order_by('id')
        serializer = Inorganic_FertilizersSerializer(Inorganic_Fertilizers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Inorganic_FertilizersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Inorganic_Fertilizers_detail(request,pk):
    try:
        Inorganic_Fertilizers = Inorganic_Fertilizers.objects.get(pk=pk)
    except Inorganic_Fertilizers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Inorganic_FertilizersSerializer(Inorganic_Fertilizers)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Inorganic_FertilizersSerializer(Inorganic_Fertilizers,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Inorganic_Fertilizer_Vendor(APIView):
    def get(self, request):
        Inorganic_Fertlizer_Vendors = Inorganic_Fertlizer_Vendor.objects.all().order_by('id')
        serializer = Inorganic_Fertlizer_VendorSerializer(Inorganic_Fertlizer_Vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Inorganic_Fertlizer_VendorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Inorganic_Fertlizer_Vendor_detail(request,pk):
    try:
        Inorganic_Fertlizer_Vendors = Inorganic_Fertlizer_Vendor.objects.get(pk=pk)
    except Inorganic_Fertlizer_Vendors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Inorganic_Fertlizer_VendorSerializer(Inorganic_Fertilizer_Vendors)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Inorganic_Fertlizer_VendorSerializer(Inorganic_Fertilizer_Vendors,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Organic_Fertlizers(APIView):
    def get(self, request):
        Organic_Fertilizers = organic_fertilizers.objects.all().order_by('id')
        serializer = Organic_FertilizersSerializer(Organic_Fertilizers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Organic_FertilizersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Organic_Fertilizers_detail(request,pk):
    try:
        Organic_Fertilizers = organic_fertilizers.objects.get(pk=pk)
    except Organic_Fertilizers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Organic_FertilizersSerializer(Organic_Fertilizers)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Organic_FertilizersSerializer(Organic_Fertilizers,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Organic_Fertlizer_Vendor(APIView):
    def get(self, request):
        Organic_Fertlizer_Vendor = organic_fertilizer_vendor.objects.all().order_by('id')
        serializer = Organic_Fertlizer_VendorSerializer(Organic_Fertlizer_Vendor, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Organic_Fertlizer_VendorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Organic_Fertilizer_Vendor_detail(request,pk):
    try:
        Organic_Fertlizer_Vendor = organic_fertilizer_vendor.objects.get(pk=pk)
    except Organic_Fertlizer_Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Organic_Fertlizer_VendorSerializer(Organic_Fertlizer_Vendor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Organic_Fertlizer_VendorSerializer(Organic_Fertlizer_Vendor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Soil_Test(APIView):
    def get(self, request):
        Soil_Test = soil_test.objects.all().order_by('id')
        serializer = Soil_TestSerializer(Soil_Test, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Soil_TestSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Soil_Test_detail(request,pk):
    try:
        Soil_Test = soil_test.objects.get(pk=pk)
    except Soil_Test.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Soil_TestSerializer(Soil_Test)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Soil_TestSerializer(Soil_Test,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Equipment_Mapping(APIView):
    def get(self, request):
        Equipment_Mapping = equipment_mapping.objects.all().order_by('id')
        serializer = Equipment_MappingSerializer(Equipment_Mapping, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Equipment_MappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Equipment_Mapping_detail(request,pk):
    try:
        Equipment_Mapping = equipment_mapping.objects.get(pk=pk)
    except Equipment_Mapping.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Equipment_MappingSerializer(Equipment_Mapping)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Equipment_MappingSerializer(Equipment_Mapping,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Organic_Fertlizers_Mapping(APIView):
    def get(self, request):
        Organic_Fertilizers_Mapping = organic_fertilizers_mapping.objects.all().order_by('id')
        serializer = Organic_Fertilizers_MappingSerializer(Organic_Fertilizers_Mapping, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Organic_Fertilizers_MappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Organic_Fertilizers_Mapping_detail(request,pk):
    try:
        Organic_Fertilizers_Mapping = organic_fertilizers_mapping.objects.get(pk=pk)
    except Organic_Fertilizers_Mapping.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Organic_Fertilizers_MappingSerializer(Organic_Fertilizers_Mapping)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Organic_Fertilizers_MappingSerializer(Organic_Fertilizers_Mapping,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Inorganic_Fertilizers_Mapping(APIView):
    def get(self, request):
        Inorganic_Fertilizers_Mapping = inorganic_fertilizers_mapping.objects.all().order_by('id')
        serializer = Inorganic_Fertilizers_MappingSerializer(Inorganic_Fertilizers_Mapping, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Inorganic_Fertilizers_MappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Inorganic_Fertilizers_Mapping_detail(request,pk):
    try:
        Inorganic_Fertilizers_Mapping = inorganic_fertilizers_mapping.objects.get(pk=pk)
    except Inorganic_Fertilizers_Mapping.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Inorganic_Fertilizers_MappingSerializer(Inorganic_Fertilizers_Mapping)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Inorganic_Fertilizers_MappingSerializer(Inorganic_Fertilizers_Mapping,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Pesticides_Mapping(APIView):
    def get(self, request):
        Pesticides_Mapping = pesticides_mapping.objects.all().order_by('id')
        serializer = Pesticides_MappingSerializer(Pesticides_Mapping, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Pesticides_MappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Pesticides_Mapping_detail(request,pk):
    try:
        Pesticides_Mapping = pesticides_mapping.objects.get(pk=pk)
    except Pesticides_Mapping.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Pesticides_MappingSerializer(Pesticides_Mapping)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Pesticides_MappingSerializer(Pesticides_Mapping,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Seeds_Mapping(APIView):
    def get(self, request):
        Seeds_Mapping = seeds_mapping.objects.all().order_by('id')
        serializer = Seeds_MappingSerializer(Seeds_MappingSerializer, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Seeds_MappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Seeds_Mapping_detail(request,pk):
    try:
        Seeds_Mapping = seeds_mapping.objects.get(pk=pk)
    except Seeds_Mapping.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Seeds_MappingSerializer(Seeds_Mapping)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Seeds_MappingSerializer(Seeds_Mapping,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Season_Mapping(APIView):
    def get(self, request):
        Season_Mapping = season_mapping.objects.all().order_by('id')
        serializer = Season_MappingSerializer(Season_Mapping, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Season_MappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Season_Mapping_detail(request,pk):
    try:
        Season_Mapping = season_mapping.objects.get(pk=pk)
    except Season_Mapping.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Season_MappingSerializer(Season_Mapping)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Season_MappingSerializer(Season_Mapping,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Potential_Market(APIView):
    def get(self, request):
        Potential_Market = potential_market.objects.all().order_by('id')
        serializer = Potential_MarketSerializer(Potential_Market, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Potential_MarketSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Potential_Market_detail(request,pk):
    try:
        Potential_Market = potential_market.objects.get(pk=pk)
    except Potential_Market.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Potential_MarketSerializer(Potential_Market)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Potential_MarketSerializer(Potential_Market,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Equipment_Available(APIView):
    def get(self, request):
        Equipment_Available = equipment_available.objects.all().order_by('id')
        serializer = Equipment_AvailableSerializer(Equipment_Available, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Equipment_AvailableSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Equipment_Available_detail(request,pk):
    try:
        Equipment_Available = equipment_available.objects.get(pk=pk)
    except Equipment_Available.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Equipment_AvailableSerializer(Equipment_Available)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Equipment_AvailableSerializer(Equipment_Available,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Inorganic_Fertilizers_Available(APIView):
    def get(self, request):
        Inorganic_Fertilizers_Available = inorganic_fertilizers_available.objects.all().order_by('id')
        serializer = Inorganic_Fertilizers_AvailableSerializer(Inorganic_Fertilizers_Available, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Inorganic_Fertilizers_AvailableSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Inorganic_Fertilizers_Available_detail(request,pk):
    try:
        Inorganic_Fertilizers_Available = inorganic_fertilizers_available.objects.get(pk=pk)
    except Inorganic_Fertilizers_Available.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Inorganic_Fertilizers_AvailableSerializer(Inorganic_Fertilizers_Available)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Inorganic_Fertilizers_AvailableSerializer(Inorganic_Fertilizers_Available,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Organic_Fertlizers_Available(APIView):
    def get(self, request):
        Organic_Fertilizers_Available = organic_fertilizers_available.objects.all().order_by('id')
        serializer = Organic_Fertilizers_AvailableSerializer(Organic_Fertilizers_Available, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Organic_Fertilizers_AvailableSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Organic_Fertilizers_Available_detail(request,pk):
    try:
        Organic_Fertilizers_Available = organic_fertilizers_available.objects.get(pk=pk)
    except Organic_Fertilizers_Available.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Organic_Fertilizers_AvailableSerializer(Organic_Fertilizers_Available)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Organic_Fertilizers_AvailableSerializer(Organic_Fertilizers_Available,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Pesticides_Available(APIView):
    def get(self, request):
        Pesticides_Available = pesticides_available.objects.all().order_by('id')
        serializer = Pesticides_AvailableSerializer(Pesticides_Available, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Pesticides_AvailableSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Pesticides_Available_detail(request,pk):
    try:
        Pesticides_Available = pesticides_available.objects.get(pk=pk)
    except Pesticides_Available.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Pesticides_AvailableSerializer(Pesticides_Available)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Pesticides_AvailableSerializer(Pesticides_Available,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Seeds_Available(APIView):
    def get(self, request):
        Seeds_Available = seeds_available.objects.all().order_by('id')
        serializer = Seeds_AvailableSerializer(Seeds_Available, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Seeds_AvailableSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def Seeds_Available_detail(request,pk):
    try:
        Seeds_Available = seeds_available.objects.get(pk=pk)
    except Seeds_Available.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Seeds_AvailableSerializer(Seeds_Available)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Seeds_AvailableSerializer(Seeds_Available,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)