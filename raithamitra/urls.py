"""raithamitra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.urls import re_path as url
from rmapp import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers, serializers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    url(r'^api/Customer/', views.API_Customer.as_view()),
    url(r'^api/Crops/', views.API_Crop.as_view()),
    url(r'^api/Land/', views.API_Land.as_view()),
    url(r'^api/Seasons/', views.API_Season.as_view()),
    url(r'^api/Labourers/', views.API_Labourer.as_view()),
    url(r'^api/Equipments/', views.API_Equipment.as_view()),
    url(r'^api/Equipment_Vendors/', views.API_Equipment_Vendor.as_view()),
    url(r'^api/Seeds/', views.API_Seed.as_view()),
    url(r'^api/Seeds_Vendors/', views.API_Seeds_Vendor.as_view()),
    url(r'^api/Pesticides/', views.API_Pesticides.as_view()),
    url(r'^api/Pesticides_Vendors/', views.API_Pesticides_Vendor.as_view()),
    url(r'^api/Inorganic_Fertilizers/', views.API_Inorganic_Fertilizers.as_view()),
    url(r'^api/Inorganic_Fertilizers_Vendors/', views.API_Inorganic_Fertilizer_Vendor.as_view()),
    url(r'^api/Organic_Fertilizers/', views.API_Organic_Fertlizers.as_view()),
    url(r'^api/Organic_Fertilizers_Vendors/', views.API_Organic_Fertlizer_Vendor.as_view()),
    url(r'^api/Soil_Test/', views.API_Soil_Test.as_view()),
    url(r'^api/Equipment_Mapping/', views.API_Equipment_Mapping.as_view()),
    url(r'^api/organic_fertilizers_mapping/', views.API_Organic_Fertlizers_Mapping.as_view()),
    url(r'^api/inorganic_fertilizers_mapping/', views.API_Inorganic_Fertilizers_Mapping.as_view()),
    url(r'^api/pesticides_mapping/', views.API_Pesticides_Mapping.as_view()),
    url(r'^api/seeds_mapping/', views.API_Seeds_Mapping.as_view()),
    url(r'^api/season_mapping/', views.API_Season_Mapping.as_view()),
    url(r'^api/potential_market/', views.API_Potential_Market.as_view()),
    url(r'^api/equipment_available/', views.API_Equipment_Available.as_view()),
    url(r'^api/inorganic_fertilizers_available/', views.API_Inorganic_Fertilizers_Available.as_view()),
    url(r'^api/organic_fertilizers_available/', views.API_Organic_Fertlizers_Available.as_view()),
    url(r'^api/pesticides_available/', views.API_Pesticides_Available.as_view()),
    url(r'^api/seeds_available/', views.API_Seeds_Available.as_view()),
    path('Customers/<int:pk>',views.customer_detail),
    path('Crops/<int:pk>', views.Crop_detail),
    path('Lands/<int:pk>',views.Land_detail),
    path('Seasons/<int:pk>', views.Season_detail),
    path('Labourers/<int:pk>', views.Labourer_detail),
    path('Equipments/<int:pk>', views.Equipment_detail),
    path('Equipment_Vendors/<int:pk>', views.Equipment_Vendor_detail),
    path('Seeds/<int:pk>', views.Seed_detail),
    path('Seeds_vendors/<int:pk>', views.Seeds_Vendor),
    path('Pesticides/<int:pk>', views.Pesticides_detail),
    path('Pesticides_Vendords/<int:pk>', views.Pesticides_Vendor_detail),
    path('Inorganic_Fertilizers/<int:pk>', views.Inorganic_Fertilizers_detail),
    path('Inorganic_Fertilizers_Vendors/<int:pk>', views.Inorganic_Fertlizer_Vendor_detail),
    path('Organic_Fertilizers/<int:pk>', views.Organic_Fertilizers_detail),
    path('Organic_Fertilizers_Vendors/<int:pk>', views.Organic_Fertilizer_Vendor_detail),
    path('Soil_Tests/<int:pk>', views.Soil_Test_detail),
    path('Equipment_Mapping/<int:pk>', views.Equipment_Mapping_detail),
    path('Organic_Fertilizer_Mapping/<int:pk>', views.Organic_Fertilizers_Mapping_detail),
    path('Inorganic_Fertilizer_Mapping/<int:pk>', views.Inorganic_Fertilizers_Mapping_detail),
    path('Pesticides_Mapping/<int:pk>', views.Pesticides_Mapping_detail),
    path('Seeds_Mapping/<int:pk>', views.Seeds_Mapping_detail),
    path('Season_Mapping/<int:pk>', views.Season_Mapping_detail),
    path('Potential_Markets/<int:pk>',views.Potential_Market_detail),
    path('Equipment_Available/<int:pk>',views.Equipment_Available_detail),
    path('Inorganic_Fertilizers_Available/<int:pk>', views.Inorganic_Fertilizers_Available_detail),
    path('Organic_Fertilizers_Available/<int:pk>', views.Organic_Fertilizers_Available_detail),
    path('Pesticides_Available/<int:pk>', views.Pesticides_Available_detail),
    path('Seeds_Available/<int:pk>', views.Seeds_Available_detail),
    path('Customer_list', views.CustomerListView.as_view(), name='customer_list'),
    path('add_profile/', views.CustomerCreateView.as_view(), name='add_profile'),
    path('update_profile/<int:pk>', views.CustomerUpdateView.as_view(), name='update_profile'),
]
