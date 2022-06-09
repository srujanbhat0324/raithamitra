# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class AppUserManager(BaseUserManager):

    def create_superuser(self, email, branch_code, staff_id, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user (email, branch_code, staff_id, password, **other_fields)

    def create_user( self, email, branch_code, staff_id, password, **other_fields):
        if not email:
            raise ValueError('You must provide a valid email address')

        email = self.normalize_email(email)
        user = self.model(email = email, branch_code = branch_code, staff_id = staff_id, ** other_fields)
        user.set_password(password)
        user.save()
        return user


class AppUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=80, null=True, verbose_name = "First Name")
    last_name = models.CharField(max_length=80, null=True, verbose_name = "Last Name")
    branch_code = models.CharField(max_length=20, null=True, verbose_name = "Branch Code")
    staff_id =  models.CharField(max_length=20, null=True, verbose_name = "Staff Id")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    start_date = models.DateTimeField(default=timezone.now)

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['branch_code', 'staff_id']

    def __str__(self):
        return self.staff_id


class Customer(models.Model):

    Gender = (('M', 'Male'),
    ('F', 'Female'),
    ('O','Other'))

    Ratings = (('1', '*'),
        ('2','**'),
        ('3','***'),
        ('4','****'),
        ('5','*****'))

    Status = (('NEW', 'New'),
            ('REPEAT', 'Repeat'),
            ('DORMANT', 'Dormant'),
            ('BLACK-LISTED', 'In Black List'))

    customer_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Customer Name")
    customer_address = models.CharField(max_length=120, blank=True, null=True,verbose_name="Customer Address")
    customer_pri_phone = models.CharField(max_length=13, blank=True,null=True,verbose_name="Customer Primary Phone")
    customer_sec_phone = models.CharField(max_length=13,blank=True,null=True,verbose_name="Customer Secondary Phone")
    customer_dob = models.DateField(blank=True,null=True,verbose_name="DOB")
    customer_gender = models.CharField(max_length=1, choices=Gender , default='M', verbose_name="Gender")
    customer_email = models.EmailField(blank=True, null=True, verbose_name= "Email Address")
    customer_status = models.CharField(max_length=20, choices=Status, default= 'NEW', verbose_name="Customer Status")
    customer_notes = models.CharField(max_length=200, blank=True, null=True, verbose_name= "Customer Notes")
    customer_rating = models.CharField(max_length=1, choices=Ratings, default='5', verbose_name="Customer Rating")

    def __str__(self):
        return self.customer_name

class Labourers(models.Model):
    labourers_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Labourers Name")
    labourers_phone = models.CharField(max_length=13, blank=True,null=True,verbose_name="Labourers Phone")
    labourers_village = models.DateField(blank=True,null=True,verbose_name="village")
    labourers_taluk = models.CharField(max_length=100, verbose_name="taluk")
    labourers_district = models.CharField(max_length=50,blank=True, null=True, verbose_name= "District")
    labourers_pincode = models.CharField(max_length=20, choices=Status, default= 'NEW', verbose_name="Labourers Pincode")
    labourers_Specialize_in_certain_work = models.CharField(max_length=200, blank=True, null=True, verbose_name= "Labourers spacilize in work")
    labourers_availability = models.CharField(max_length=1, choices=Ratings, default='5', verbose_name="Labourers Availability")

    def __str__(self):
        return self.labourers_name



class Equipment_Vendors()
    vendors_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Vendors Name")
    vendors_phone = models.CharField(max_length=13, blank=True,null=True,verbose_name="Vendors Phone")
    vendors_email_id = models.CharField(max_length=13, blank=True,null=True,verbose_name="Vendors Email Id")
    vendors_village= models.CharField(max_length=13,blank=True,null=True,verbose_name="Village")
    vendors_taluk = models.DateField(blank=True,null=True,verbose_name="Taluk")
    vendors_district = models.CharField(max_length=1, choices=Gender , default='M', verbose_name="District")
    vendors_pincode = models.EmailField(blank=True, null=True, verbose_name= "Vendors Pincode")
    vendors_shop_name = models.CharField(max_length=20, choices=Status, default= 'NEW', verbose_name="Vendors Shop Nme")
    vendors_avilability= models.CharField(max_length=200, blank=True, null=True, verbose_name= "Vendors Avilability")
    vendors_rating_and_reveiws= models.CharField(max_length=1, choices=Ratings, default='5', verbose_name="Vendors Rating")

    def __str__(self):
        return self.equipment_vender_name
    
    

class seeds_vendor(models.Model):

    seeds_vendor_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=" seeds vendor Name")
    shop_name = models.CharField(max_length=120, blank=True, null=True,verbose_name="shop name")
    seeds_vendor_village = models.CharField(max_length=13, blank=True,null=True,verbose_name="seeds vendor_village")
    seeds_vendor_taluk = models.CharField(max_length=13,blank=True,null=True,verbose_name="seeds vendor_taluk")
    seeds_vendor_district = models.CharField(max_length=1,blank=True,null=True,verbose_name="seeds vendor_district")
    seeds_vendor_pincode = models.CharField(max_length=20,blank=True,null=True,verbose_name="seeds vendor_pincode")
    seeds_vendor_availability = models.CharField(max_length=200, blank=True, null=True, verbose_name= "seeds vendor_availability")
    
    def __str__(self):
        return self.seeds_vendor_name
    
class Crop(models.Model):    
class Crop(models.Model):
class Pestisides(models.Model):

     pestisides_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Pestisides name")
     pestisides_cost = models.CharField(max_length=120, blank=True, null=True,verbose_name="Pestisides cost")
     pestisises_methods_to_use = models.CharField(max_length=13, blank=True,null=True,verbose_name="pestisides methods to use")

def __str__(self):
        return self.pestides_name     

class Equipments(models.Model):

    equipments_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="equipments Name")
    equipments_type = models.CharField(max_length=2, blank=True, null=True,verbose_name="equipments type of equipments")
    equipments_cost= models.CharField(max_length=13, blank=True,null=True,verbose_name="equipments cost")
    equipments_life_time = models.CharField(max_length=13,blank=True,null=True,verbose_name="Lifetime Of Equipments")

    def __str__(self):
        return self.equipments_name  

 class Inorganic_Fertilizers(models.Model):

    fertilizers_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=" fertilizers name")
    fertilizers_cost= models.CharField(max_length=120, blank=True, null=True,verbose_name="fertilizers cost")
    fertilizers_methods_to_use = models.CharField(max_length=13, blank=True,null=True,verbose_name="fertilizers methods to use")
    fertilizers_diffrent_types = models.CharField(max_length=13,blank=True,null=True,verbose_name="fertilizers diffrent types") 


  def __str__(self):
        return self.fertilizers_name

 
    
class Crop(models.Model):  

    Type = (('Fo','Food Crop'),
        ('Fe','Feed Crop'),
        ('Fi','Fiber Crop'),
        ('Oi','Oil Crop'),
        ('Or','Ornamental Crop'),
        ('In','Industrial Crop'))

    crop_name = models.CharField(max_length=100, blank= True, null=True,verbose_name="Crop Name")
    crop_description = models.CharField(max_length=200, blank=True, null=True, verbose_name= "Crop Description")
    crop_type = models.CharField(max_length=2, choices=Type , default='Fo', verbose_name="Crop Type")
    crop_average_rate_in_market = models.CharField(max_length=15, blank=True,null=True,verbose_name="Crop Average Rate In Market")
    crop_cost_to_grow = models.CharField(max_length=14, blank=True,null=True,verbose_name="Crop Cost To Grow")
    crop_diseases = models.CharField(max_length=200, blank=True, null=True, verbose_name= "Crop Diseases")
    crop_seeds_per_acre = models.CharField(max_length=14,blank=True,null=True,verbose_name="Crop Seeds Per Acre")

    def __str__(self):
        return self.crop_name

class Lands(models.Model):

    Type = (('Ar','Arable Crop Land'),
        ('Pr','Permanent Crop Land'),
        ('Pe','Permanent Grassland'))

    land_type = models.CharField(max_length=2, choices=Type, default='Ar' verbose_name="Land Type")
    land_description = models.CharField(max_length=200, blank=True, null=True,verbose_name="Land Description")
    land_details = models.CharField(max_length=200, blank=True,null=True,verbose_name="Land Details")
    land_suitable_crop_details = models.CharField(max_length=120, blank=True, null=True,verbose_name="Crop Suitable Land Details")

    def __str__(self):
        return self.land_details
    
    