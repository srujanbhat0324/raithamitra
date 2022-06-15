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

@api_view(['GET','PUT'])
def customer_detail(request,pk):
    try:
        Customer = customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(Customer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(Customer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
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

class API_Seed(APIView):
    def get(self, request):
        Seed = seed.objects.all().order_by('id')
        serializer = SeedSerializer(Seed, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = SeedSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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

class API_Pesticides(APIView):
    def get(self, request):
        Pesticides = pesticides.objects.all().order_by('id')
        serializer = PesticidesSerializer(Pesticides, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = PesticidesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Pesticides_Vendor(APIView):
    def get(self, request):
        Pesticides_Vendor = pesticides_vendor.objects.all().order_by('id')
        serializer = Pesticides_VendorSerializer(Pesticides_Vendor, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Pesticides_VendorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Inorganic_Fertilizers(APIView):
    def get(self, request):
        Inorganic_Fertilizers = inorganic_fertilizers.objects.all().order_by('id')
        serializer = Inorganic_FertilizersSerializer(Inorganic_Fertilizers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Inorganic_FertilizersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class API_Inorganic_Fertilizer_Vendor(APIView):
    def get(self, request):
        Inorganic_Fertlizer_Vendor = inorganic_fertlizer_vendor.objects.all().order_by('id')
        serializer = Inorganic_Fertlizer_VendorSerializer(Inorganic_Fertlizer_Vendor, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = Inorganic_FertilizersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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