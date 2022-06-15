from rest_framework import serializers
from rmapp.models import AppUser, Customer, Crop, Land, Season, Labourer, Equipment, Equipment_Vendor, Seed, Seeds_Vendor, Pesticides, Pesticides_Vendor, Inorganic_Fertilizers, Inorganic_Fertlizer_Vendor, Organic_Fertilizers, Organic_Fertlizer_Vendor,  Soil_Test, Equipment_Mapping, Organic_Fertilizers_Mapping, Inorganic_Fertilizers_Mapping, Pesticides_Mapping, Seeds_Mapping, Season_Mapping, Potential_Market, Equipment_Available, Inorganic_Fertilizers_Available, Organic_Fertilizers_Available, Pesticides_Available, Seeds_Available

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'

class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'

class LabourerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labourer
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class Equipment_VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment_Vendor
        fields = '__all__'

class SeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seed
        fields = '__all__'

class Seeds_VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seeds_Vendor
        fields = '__all__'

class PesticidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesticides
        fields = '__all__'

class Pesticides_VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesticides_Vendor
        fields = '__all__'

class Inorganic_FertilizersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inorganic_Fertilizers
        fields = '__all__'

class Inorganic_Fertlizer_VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inorganic_Fertlizer_Vendor
        fields = '__all__'

class Organic_FertilizersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organic_Fertilizers
        fields = '__all__'

class  Organic_Fertlizer_VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organic_Fertlizer_Vendor
        fields  = '__all__'

class Soil_TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soil_Test
        fields = '__all__'

class Equipment_MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment_Mapping
        fields = '__all__'

class Organic_Fertilizers_MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organic_Fertilizers_Mapping
        fields = '__all__'

class Inorganic_Fertilizers_MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inorganic_Fertilizers_Mapping
        fields = '__all__'

class Pesticides_MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesticides_Mapping
        fields = '__all__'

class Seeds_MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seeds_Mapping
        fields = '__all__'

class Season_MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season_Mapping
        fields = '__all__'

class Potential_MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Potential_Market
        fields = '__all__'

class Equipment_AvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment_Available
        fields = '__all__'

class Organic_Fertilizers_AvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organic_Fertilizers_Available
        fields = '__all__'

class Inorganic_Fertilizers_AvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inorganic_Fertilizers_Available
        fields = '__all__'

class Pesticides_AvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesticides_Available
        fields = '__all__'

class Seeds_AvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seeds_Available
        fields = '__all__'
