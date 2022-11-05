# Create your filters here.
###################################################
# ****Copyright 2022 - Raitha Mitra/ SDCP****
# Accfina DMS
# Filters Set up
# November 2022
# Author : Srujan Bhat
###################################################


from .models import Customer
import django_filters


class CustomerFilterSet(django_filters.FilterSet):
    customer_name = django_filters.CharFilter(lookup_expr='icontains')
    customer_village = django_filters.CharFilter(lookup_expr='icontains')
    customer_pri_phone = django_filters.CharFilter(lookup_expr='icontains')
    customer_email= django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_village', 'customer_pri_phone', 'customer_email']

