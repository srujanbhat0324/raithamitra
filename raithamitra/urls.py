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
    url(r'^api/customers/', views.API_Customer.as_view()),
    url(r'^api/crops/', views.API_Crop.as_view()),
    url(r'^api/lands/', views.API_Land.as_view()),
    url(r'^api/seasons/', views.API_Season.as_view()),
    url(r'^api/labourers/', views.API_Labourer.as_view()),
    url(r'^api/equipments/', views.API_Equipment.as_view()),
    url(r'^api/equipment_vendors/', views.API_Equipment_Vendor.as_view()),
    url(r'^api/seeds/', views.API_Seed.as_view()),
    url(r'^api/seeds_vendors/', views.API_Seeds_Vendor.as_view()),
    url(r'^api/pesticides/', views.API_Pesticides.as_view()),
    url(r'^api/pesticides_vendors/', views.API_Pesticides_Vendor.as_view()),
    url(r'^api/inorganic_fertilizers/', views.API_Inorganic_Fertilizers.as_view()),
    url(r'^api/inorganic_fertilizers_vendors/', views.API_Inorganic_Fertilizer_Vendor.as_view()),
    url(r'^api/organic_fertilizers/', views.API_Organic_Fertlizers.as_view()),
    url(r'^api/organic_fertilizers_vendors/', views.API_Organic_Fertlizer_Vendor.as_view()),
    url(r'^api/soil_test/', views.API_Soil_Test.as_view()),
    url(r'^api/equipment_mapping/', views.API_Equipment_Mapping.as_view()),
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
]
