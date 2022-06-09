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
    
    