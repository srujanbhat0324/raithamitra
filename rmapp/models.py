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
    customer_village = models.CharField(max_length=50,blank=True,null=True,verbose_name="Village")
    customer_taluk = models.CharField(max_length=100, blank=True,null=True,verbose_name="Taluk")
    customer_district = models.CharField(max_length=50,blank=True, null=True, verbose_name= "District")
    customer_pincode = models.CharField(max_length=20, blank=True,null=True, verbose_name="Pincode")
    customer_pri_phone = models.CharField(max_length=13, blank=True,null=True,verbose_name="Customer Primary Phone")
    customer_sec_phone = models.CharField(max_length=13,blank=True,null=True,verbose_name="Customer Secondary Phone")
    customer_dob = models.DateField(blank=True,null=True,verbose_name="DOB")
    customer_gender = models.CharField(max_length=1, choices=Gender , default='M', verbose_name="Gender")
    customer_email = models.EmailField(blank=True, null=True, verbose_name= "Email Address")
    customer_status = models.CharField(max_length=20, choices=Status, default= 'NEW', verbose_name="Customer Status")
    customer_notes = models.CharField(max_length=200, blank=True, null=True, verbose_name= "Customer Notes")
    customer_rating = models.CharField(max_length=1, choices=Ratings, default='5', verbose_name="Customer Rating")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.customer_name

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
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.crop_name

class Land(models.Model):

    Type = (('Ar','Arable Crop Land'),
        ('Pr','Permanent Crop Land'),
        ('Pe','Permanent Grassland'))

    land_type = models.CharField(max_length=2, choices=Type, default='Ar', verbose_name="Land Type")
    land_description = models.CharField(max_length=200, blank=True, null=True,verbose_name="Land Description")
    land_details = models.CharField(max_length=200, blank=True,null=True,verbose_name="Land Details")
    land_suitable_crop_details = models.CharField(max_length=120, blank=True, null=True,verbose_name="Crop Suitable Land Details")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.land_details

class Season(models.Model):

    Type = (('Su','Summer Season'),
        ('Wi','Winter Season'),
        ('Au','Autumn Season'),
        ('Sp','Spring season'),
        ('Dr','Dry Season'),
        ('At','Atlantic Hurricane Season'))

    season_type = models.CharField(max_length=2,choices=Type, default='Su', verbose_name="Season Type")
    season_description = models.CharField(max_length=300,blank=True, null=True, verbose_name="Season Description")
    season_suitable_crop_details = models.CharField(max_length=50, blank=True, null=True, verbose_name="Crop Suitable Season Details")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.season_type


class Farming_Methods(models.Model):

    Type = (('So','Soil Preparation'),
        ('Sw','Sowing'),
        ('Ma','Manuring'),
        ('Ir','Irrigation'),
        ('We','Weeding'),
        ('Ha','Harvesting'),
        ('St','Storage'))

    method_type = models.CharField(max_length=2, choices=Type, default='So', verbose_name="Main Farming Methods  Type")
    method_description = models.CharField(max_length=300,blank=True,null=True, verbose_name="Method Description")
    crop_name = models.ForeignKey(Crop,on_delete=models.PROTECT,null=True, verbose_name= "Crop Name")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.method_type



class Labourer(models.Model):

    Gender = (('M','Male'),
        ('F','Female'))

    labourer_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Labourer Name")
    labourer_phone = models.CharField(max_length=13, blank=True,null=True,verbose_name="Labourer Phone")
    labourer_village = models.CharField(max_length=50,blank=True,null=True,verbose_name="Village")
    labourer_taluk = models.CharField(max_length=100, blank=True,null=True,verbose_name="Taluk")
    labourer_district = models.CharField(max_length=50,blank=True, null=True, verbose_name= "District")
    labourer_pincode = models.CharField(max_length=20, blank=True,null=True, verbose_name="Pincode")
    labourer_gender = models.CharField(max_length=1, choices=Gender , default='M', verbose_name="Gender")
    labourer_Specialize_in_certain_work = models.CharField(max_length=200, blank=True, null=True, verbose_name= "Specialize in Certain Work")
    labourer_availability = models.CharField(max_length=50,blank=True,null=True, verbose_name="Labourer Availability")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.labourer_name

class Equipment(models.Model):

    Type = (('Tr','Tractor'),
        ('Co','Combine Harvester'),
        ('Pl','Plough'),
        ('Sp','Sprayer'),
        ('Cu','Cultivator'),
        ('Ir','Irrigation'),
        ('Ha','Harrow'),
        ('Ba','Baler'),
        ('Se','Seed Drill'),
        ('Di','Disc Harrow'),
        ('Br','Broadcast Spreader'),
        ('Ra','Rake'),
        ('Ma','Manure spreader'),
        ('Ro','Rotary Tiller'),
        ('Pt','Plant'),
        ('Sd','Seed'),
        ('We','Weeder'),
        ('Bc','Backhoe'),
        ('Pe','Power Tiller'),
        ('Ps','Paper Shredder'),
        ('Tm','Threshing Machine'),
        ('Cu','Cultipacker'),
        ('Lo','Loader'),
        ('Sh','Shovel'))

    equipment_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Equipment Name")
    equipment_type = models.CharField(max_length=2, choices=Type, default='Tr',verbose_name="Type of Equipment")
    equipment_cost= models.CharField(max_length=13, blank=True,null=True,verbose_name="Equipment cost")
    equipment_life_time = models.CharField(max_length=13,blank=True,null=True,verbose_name="Lifetime Of Equipment")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.equipment_name

class Equipment_Vendor(models.Model):

    Ratings = (('1', '*'),
        ('2','**'),
        ('3','***'),
        ('4','****'),
        ('5','*****'))

    equipment_name = models.ForeignKey(Equipment, on_delete=models.PROTECT, null=True,verbose_name="Equipment Name")
    vendor_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Vendor Name")
    vendor_phone = models.CharField(max_length=13, blank=True,null=True,verbose_name="Phone Number")
    vendor_email_id = models.EmailField(max_length=50, blank=True,null=True,verbose_name="Email Id")
    vendor_village= models.CharField(max_length=50,blank=True,null=True,verbose_name="Village")
    vendor_taluk = models.CharField(max_length=50,blank=True,null=True,verbose_name="Taluk")
    vendor_district = models.CharField(max_length=100,blank=True,null=True, verbose_name="District")
    vendor_pincode = models.CharField(max_length=20,blank=True, null=True, verbose_name= "Pincode")
    vendor_shop_name = models.CharField(max_length=200,blank=True, null=True , verbose_name="Shop Name")
    vendor_availability= models.CharField(max_length=200, blank=True, null=True, verbose_name= "Vendor Availability")
    vendor_review = models.CharField(max_length=200, blank=True, null=True, verbose_name= "Vendor Review")
    vendor_rating= models.CharField(max_length=1, choices=Ratings, default='5', verbose_name="Vendors Rating")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.vendor_name
    

class Seed(models.Model):

    Type =  (('Wh','Wheat'),
        ('Ma','Maize'),
        ('Pa','Paddy'),
        ('Gr','Groundnut'),
        ('Pe','Pearl Millet'),
        ('Ba','Barley'),
        ('So','Soybean'),
        ('Mu','Mung Bean'),
        ('Ps','Peas'),
        ('Vi','Vigna Mungo'),
        ('Su','Sunflower'),
        ('Sr','Sorghum'),
        ('Co','Cowpea'),
        ('Ra','Ragi'),
        ('Jo','Jowar'),
        ('Li','Linseed'),
        ('Mi','Millets'),
        ('Le','Lentil'),
        ('Ar','Araikeerai Seed'))

    seed_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Seed Name")
    seed_type = models.CharField(max_length=2,choices=Type, default='Wh', verbose_name="Seed Type")
    seed_description = models.CharField(max_length=300,null=True,blank=True,verbose_name="Seed Description")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.seed_name


class Seeds_Vendor(models.Model):

    Ratings = (('1', '*'),
        ('2','**'),
        ('3','***'),
        ('4','****'),
        ('5','*****'))

    seed_name = models.ForeignKey(Seed, on_delete=models.PROTECT , null=True , verbose_name="Seed Name")
    vendor_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Vendor Name")
    vendor_phone = models.CharField(max_length=13, blank=True,null=True,verbose_name="Phone Number")
    vendor_email_id = models.EmailField(max_length=50, blank=True,null=True,verbose_name="Email Id")
    vendor_village= models.CharField(max_length=50,blank=True,null=True,verbose_name="Village")
    vendor_taluk = models.CharField(max_length=50,blank=True,null=True,verbose_name="Taluk")
    vendor_district = models.CharField(max_length=100,blank=True,null=True, verbose_name="District")
    vendor_pincode = models.CharField(max_length=20,blank=True, null=True, verbose_name= "Pincode")
    vendor_shop_name = models.CharField(max_length=200,blank=True, null=True , verbose_name="Shop Name")
    vendor_availability= models.CharField(max_length=200, blank=True, null=True, verbose_name= "Vendor Availability")
    vendor_review = models.CharField(max_length=200, blank=True, null=True, verbose_name= "Vendor Review")
    vendor_rating= models.CharField(max_length=1, choices=Ratings, default='5', verbose_name="Vendor Rating")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")
    
    def __str__(self):
        return self.vendor_name
    
 

class Pesticides(models.Model):

    pesticides_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Pesticides name")
    pesticides_cost = models.CharField(max_length=20, blank=True, null=True,verbose_name="Pesticides Cost")
    pesticides_methods_to_use = models.CharField(max_length=300, blank=True,null=True,verbose_name="Methods to Use")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.pesticides_name     

  
class Pesticides_Vendor(models.Model):

    Ratings = (('1', '*'),
        ('2','**'),
        ('3','***'),
        ('4','****'),
        ('5','*****'))

    pesticides_name = models.ForeignKey(Pesticides, on_delete=models.PROTECT, null=True , verbose_name="Pesticides Name")
    vendor_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Vendor Name")
    vendor_phone = models.CharField(max_length=13, blank=True,null=True,verbose_name="Phone Number")
    vendor_email_id = models.EmailField(max_length=50, blank=True,null=True,verbose_name="Email Id")
    vendor_village= models.CharField(max_length=50,blank=True,null=True,verbose_name="Village")
    vendor_taluk = models.CharField(max_length=50,blank=True,null=True,verbose_name="Taluk")
    vendor_district = models.CharField(max_length=100,blank=True,null=True, verbose_name="District")
    vendor_pincode = models.CharField(max_length=20,blank=True, null=True, verbose_name= "Pincode")
    vendor_shop_name = models.CharField(max_length=200,blank=True, null=True , verbose_name="Shop Name")
    vendor_availability= models.CharField(max_length=200, blank=True, null=True, verbose_name= "Vendor Availability")
    vendor_review = models.CharField(max_length=200, blank=True, null=True, verbose_name= "Vendor Review")
    vendor_rating= models.CharField(max_length=1, choices=Ratings, default='5', verbose_name="Vendor Rating")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")
    
    def __str__(self):
        return self.vendor_name


class Inorganic_Fertilizers(models.Model):

    Type = (('Ni','Nitrogen Fertilizers'),
        ('Ph','Phosphorous Fertilizers'),
        ('Po','Potassium Fertilizers'),
        ('Su','Sulfur,Calcium and Magnesium Fertilizers'),
        ('Mi','Micronutrient Fertilizers'))

    fertilizer_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Fertilizer Name")
    fertilizer_type = models.CharField(max_length=2,choices=Type, default='Ni',verbose_name="Fertilizer Type")
    fertilizer_description = models.CharField(max_length=300,blank=True,null=True, verbose_name="Fertilizer Description")
    fertilizer_cost= models.CharField(max_length=120, blank=True, null=True,verbose_name="Fertilizer Cost")
    fertilizer_methods_to_use = models.CharField(max_length=300, blank=True,null=True,verbose_name="Methods to Use")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")
     


    def __str__(self):
        return self.fertilizer_name


class Inorganic_Fertlizer_Vendor(models.Model):

    Ratings = (('1', '*'),
        ('2','**'),
        ('3','***'),
        ('4','****'),
        ('5','*****'))

    fertilizer_name = models.ForeignKey(Inorganic_Fertilizers, on_delete=models.PROTECT, null=True,verbose_name="Fertilizer Name")
    vendor_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Vendor Name")
    vendor_phone = models.CharField(max_length=13, blank=True,null=True,verbose_name="Phone Number")
    vendor_email_id = models.EmailField(max_length=50, blank=True,null=True,verbose_name="Email Id")
    vendor_village= models.CharField(max_length=50,blank=True,null=True,verbose_name="Village")
    vendor_taluk = models.CharField(max_length=50,blank=True,null=True,verbose_name="Taluk")
    vendor_district = models.CharField(max_length=100,blank=True,null=True, verbose_name="District")
    vendor_pincode = models.CharField(max_length=20,blank=True, null=True, verbose_name= "Pincode")
    vendor_shop_name = models.CharField(max_length=200,blank=True, null=True , verbose_name="Shop Name")
    vendor_availability= models.CharField(max_length=200, blank=True, null=True, verbose_name= "Vendor Availability")
    vendor_review = models.CharField(max_length=200, blank=True, null=True, verbose_name= "Vendor Review")
    vendor_rating= models.CharField(max_length=1, choices=Ratings, default='5', verbose_name="Vendors Rating")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.vendor_name


class Organic_Fertilizers(models.Model):

    Type = (('Ma','Manure'),
    ('Co','Compost'),
    ('Ro','Rock Phospate'),
    ('Ch','Chicken Litter'),
    ('Bo','Bone Meal'),
    ('Ve','Vermicompost'))

    fertilizer_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Fertilizer Name")
    fertilizer_type = models.CharField(max_length=2,choices=Type, default='Ma',verbose_name="Fertilizer Type")
    fertilizer_description = models.CharField(max_length=300,blank=True,null=True, verbose_name="Fertilizer Description")
    fertilizer_cost= models.CharField(max_length=120, blank=True, null=True,verbose_name="Fertilizer Cost")
    fertilizer_methods_to_use = models.CharField(max_length=300, blank=True,null=True,verbose_name="Methods to Use")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")
    


    def __str__(self):
        return self.fertilizer_name


class Organic_Fertlizer_Vendor(models.Model):

    Ratings = (('1', '*'),
        ('2','**'),
        ('3','***'),
        ('4','****'),
        ('5','*****'))

    fertilizer_name = models.ForeignKey(Organic_Fertilizers, on_delete=models.PROTECT, null=True,verbose_name="Fertilizer Name")
    vendor_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Vendor Name")
    vendor_phone = models.CharField(max_length=13, blank=True,null=True,verbose_name="Phone Number")
    vendor_email_id = models.EmailField(max_length=50, blank=True,null=True,verbose_name="Email Id")
    vendor_village= models.CharField(max_length=50,blank=True,null=True,verbose_name="Village")
    vendor_taluk = models.CharField(max_length=50,blank=True,null=True,verbose_name="Taluk")
    vendor_district = models.CharField(max_length=100,blank=True,null=True, verbose_name="District")
    vendor_pincode = models.CharField(max_length=20,blank=True, null=True, verbose_name= "Pincode")
    vendor_shop_name = models.CharField(max_length=200,blank=True, null=True , verbose_name="Shop Name")
    vendor_availability= models.CharField(max_length=200, blank=True, null=True, verbose_name= "Vendor Availability")
    vendor_review = models.CharField(max_length=200, blank=True, null=True, verbose_name= "Vendor Review")
    vendor_rating= models.CharField(max_length=1, choices=Ratings, default='5', verbose_name="Vendors Rating")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.vendor_name


class Soil_Test(models.Model):

    Test = (('Y','Yes'),
        ('N','No'))

    test_name = models.CharField(max_length=50,blank=True,null=True,verbose_name="Test Name")
    test_done = models.BooleanField(max_length=1,choices=Test,  default='Y', verbose_name="Test Done")
    test_done_date  = models.DateField(blank=True, null=True, verbose_name="Test Conducted Date")
    test_result_date = models.DateField(blank=True, null=True, verbose_name="Test Result Date")
    test_done_by = models.CharField(max_length=50, blank=True, null=True, verbose_name="Test Done By")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.test_name

class Potential_Market(models.Model):

    Type = (('Pr','Primary Market'),
        ('Se','Secondary Market'),
        ('Te','Terminal Market'),
        ('Re','Regulated Market'),
        ('Co','Co-Operative Markets'),
        ('St','State Trading'))

    market_name = models.CharField(max_length=50, blank=True, null= True, verbose_name="Market Name")
    market_type = models.CharField(max_length=2,choices=Type, default='Pr' , verbose_name="Type of Market")
    market_village= models.CharField(max_length=50,blank=True,null=True,verbose_name="Village")
    market_taluk = models.CharField(max_length=50,blank=True,null=True,verbose_name="Taluk")
    market_district = models.CharField(max_length=100,blank=True,null=True, verbose_name="District")
    market_pincode = models.CharField(max_length=20,blank=True, null=True, verbose_name= "Pincode")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.market_name


class Equipment_Mapping(models.Model):

    equipment_name  = models.ForeignKey(Equipment,on_delete=models.PROTECT, null=True, verbose_name="Equipment Name")
    vendor_name =models.ForeignKey(Equipment_Vendor, on_delete=models.PROTECT, null=True, verbose_name="Vendor Name")
    mapping_name= models.CharField(max_length=50,blank=True,null=True, verbose_name="Mapping Name")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def _str__(self):
        return self.mapping_name


class Organic_Fertilizers_Mapping(models.Model):

    fertilizer_name  = models.ForeignKey(Organic_Fertilizers,on_delete=models.PROTECT, null=True, verbose_name="Fertilizer Name")
    vendor_name =models.ForeignKey(Organic_Fertlizer_Vendor, on_delete=models.PROTECT, null=True, verbose_name="Vendor Name")
    mapping_name= models.CharField(max_length=50,blank=True,null=True, verbose_name="Mapping Name")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def _str__(self):
        return self.mapping_name


class Inorganic_Fertilizers_Mapping(models.Model):

    fertilizer_name  = models.ForeignKey(Inorganic_Fertilizers,on_delete=models.PROTECT, null=True, verbose_name="Fertilizer Name")
    vendor_name =models.ForeignKey(Inorganic_Fertlizer_Vendor, on_delete=models.PROTECT, null=True, verbose_name="Vendor Name")
    mapping_name= models.CharField(max_length=50,blank=True,null=True, verbose_name="Mapping Name")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def _str__(self):
        return self.mapping_name

 
class Pesticides_Mapping(models.Model):

    pesticides_name  = models.ForeignKey(Pesticides,on_delete=models.PROTECT, null=True, verbose_name="Pesticides Name")
    vendor_name =models.ForeignKey(Pesticides_Vendor, on_delete=models.PROTECT, null=True, verbose_name="Vendor Name")
    mapping_name= models.CharField(max_length=50,blank=True,null=True, verbose_name="Mapping Name")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def _str__(self):
        return self.mapping_name


class Seeds_Mapping(models.Model):

    seed_name  = models.ForeignKey(Seed,on_delete=models.PROTECT, null=True, verbose_name="Seed Name")
    vendor_name =models.ForeignKey(Seeds_Vendor, on_delete=models.PROTECT, null=True, verbose_name="Vendor Name")
    mapping_name= models.CharField(max_length=50,blank=True,null=True, verbose_name="Mapping Name")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def _str__(self):
        return self.mapping_name
    

class Season_Mapping(models.Model):

    season_type  = models.ForeignKey(Season,on_delete=models.PROTECT, null=True, verbose_name="Season Name")
    crop_name =models.ForeignKey(Crop, on_delete=models.PROTECT, null=True, verbose_name="Crop Name")
    mapping_name= models.CharField(max_length=50,blank=True,null=True, verbose_name="Mapping Name")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def _str__(self):
        return self.mapping_name


class Equipment_Available(models.Model):

    mapping_name = models.ForeignKey(Equipment_Mapping,on_delete=models.PROTECT,null=True,verbose_name="Mapping Name")
    available_from = models.DateField(blank=True, null=True,verbose_name="Available From")
    available_to = models.DateField(blank=True, null=True,verbose_name="Available To")
    quantity_Available = models.CharField(max_length=10,blank=True, null=True, verbose_name="Quantity Available")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.mapping_name

class Organic_Fertilizers_Available(models.Model):

    mapping_name = models.ForeignKey(Organic_Fertilizers_Mapping,on_delete=models.PROTECT,null=True,verbose_name="Mapping Name")
    available_from = models.DateField(blank=True, null=True,verbose_name="Available From")
    available_to = models.DateField(blank=True, null=True,verbose_name="Available To")
    quantity_Available = models.CharField(max_length=10,blank=True, null=True, verbose_name="Quantity Available")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.mapping_name

class Inorganic_Fertilizers_Available(models.Model):

    mapping_name = models.ForeignKey(Inorganic_Fertilizers_Mapping,on_delete=models.PROTECT,null=True,verbose_name="Mapping Name")
    available_from = models.DateField(blank=True, null=True,verbose_name="Available From")
    available_to = models.DateField(blank=True, null=True,verbose_name="Available To")
    quantity_Available = models.CharField(max_length=10,blank=True, null=True, verbose_name="Quantity Available")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.mapping_name

class Pesticides_Available(models.Model):

    mapping_name = models.ForeignKey(Pesticides_Mapping,on_delete=models.PROTECT,null=True,verbose_name="Mapping Name")
    available_from = models.DateField(blank=True, null=True,verbose_name="Available From")
    available_to = models.DateField(blank=True, null=True,verbose_name="Available To")
    quantity_Available = models.CharField(max_length=10,blank=True, null=True, verbose_name="Quantity Available")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.mapping_name

class Seeds_Available(models.Model):

    mapping_name = models.ForeignKey(Seeds_Mapping,on_delete=models.PROTECT,null=True,verbose_name="Mapping Name")
    available_from = models.DateField(blank=True, null=True,verbose_name="Available From")
    available_to = models.DateField(blank=True, null=True,verbose_name="Available To")
    quantity_Available = models.CharField(max_length=10,blank=True, null=True, verbose_name="Quantity Available")
    added_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Added By")
    added_date_time = models.DateTimeField(default=timezone.now, verbose_name="Added Date/Time")
    updated_by = models.CharField(max_length=50,blank=True,null=True, verbose_name="Updated By")
    updated_date_time = models.DateTimeField(default=timezone.now, verbose_name="Updated Date/Time")

    def __str__(self):
        return self.mapping_name
