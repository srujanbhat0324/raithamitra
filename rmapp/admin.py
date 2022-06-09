from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AppUser, Customer, Crop, Land, Season, Labourer, Equipment, Equipment_Vendor, Seed, Seeds_Vendor, Pesticides, Pesticides_Vendor, Inorganic_Fertilizers, Inorganic_Fertlizer_Vendor, Organic_Fertilizers, Organic_Fertlizer_Vendor,  Soil_Test, Equipment_Mapping, Organic_Fertilizers_Mapping, Inorganic_Fertilizers_Mapping,Pesticides_Mapping,Seeds_Mapping, Season_Mapping, Potential_Market, Equipment_Available,Inorganic_Fertilizers_Available, Organic_Fertilizers_Available, Pesticides_Available, Seeds_Available
from django.contrib.auth.admin  import UserAdmin

# Register your models here.
class UserAdminConfig(UserAdmin):
    search_fields =('email', 'first_name', 'branch_code','staff_id',)
    list_filter = ('email', 'first_name', 'branch_code','staff_id','is_active', 'is_staff',)
    ordering =('-start_date',)
    list_display = ('email', 'first_name', 'last_name', 'branch_code','staff_id', 'is_active', 'is_staff')
    fieldsets = (
        ('User Details', {'fields':('email', 'first_name', 'last_name')}),
        ('Permissions', {'fields':('is_staff', 'is_active')}),
        ('Others', {'fields':('start_date',)}),
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','first_name', 'last_name', 'branch_code','staff_id', 'is_active', 'is_staff',),
        }),
    )
   

admin.site.register(AppUser, UserAdminConfig)
admin.site.register(Customer)
admin.site.register(Crop)
admin.site.register(Land)
admin.site.register(Season)
admin.site.register(Labourer)
admin.site.register(Equipment)
admin.site.register(Equipment_Vendor)
admin.site.register(Seed)
admin.site.register(Seeds_Vendor)
admin.site.register(Pesticides)
admin.site.register(Pesticides_Vendor)
admin.site.register(Inorganic_Fertilizers)
admin.site.register(Inorganic_Fertlizer_Vendor)
admin.site.register(Organic_Fertilizers)
admin.site.register(Organic_Fertlizer_Vendor)
admin.site.register(Soil_Test)
admin.site.register(Potential_Market)
admin.site.register(Equipment_Mapping)
admin.site.register(Organic_Fertilizers_Mapping)
admin.site.register(Inorganic_Fertilizers_Mapping)
admin.site.register(Pesticides_Mapping)
admin.site.register(Seeds_Mapping)
admin.site.register(Season_Mapping)
admin.site.register(Equipment_Available)
admin.site.register(Organic_Fertilizers_Available)
admin.site.register(Inorganic_Fertilizers_Available)
admin.site.register(Pesticides_Available)
admin.site.register(Seeds_Available)