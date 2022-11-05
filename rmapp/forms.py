# Create your forms here.
###################################################
# ****Copyright 2022 -Raitha Mitra/ SDCP****
# Accfina DMS
# Forms Set up
# November 2022
# Author : Srujan Bhat
###################################################


from django import forms
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalModelForm
from django.forms import ClearableFileInput
from .models import  Customer


class CustomerForm(BSModalModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_village', 'customer_pri_phone', 'customer_dob','customer_gender','customer_email']
        exclude = ['timestamp']

