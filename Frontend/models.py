from django.db import models
from django.utils import timezone
from Backend.models import ProductDB
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.

class RegistrationDB(models.Model):
    Username = models.CharField(max_length=50,null=True,blank=True,unique=True)
    Password = models.CharField(max_length=50,blank=True,null=True)
    Mobile_User = models.IntegerField(blank=True,null=True)
    Mail = models.EmailField(max_length=50, blank=True, null=True)
    Address = models.CharField(max_length=200,blank=True,null=True)
    Profile_Pic = models.ImageField(upload_to="User_pic",blank=True,null=True)


class SellDB(models.Model):
    Category_Name = models.CharField(max_length=50, blank=True, null=True)
    Property_place = models.CharField(max_length=100, blank=True, null=True)
    Property_Address = models.CharField(max_length=100, blank=True, null=True)
    Bedroom = models.IntegerField(blank=True, null=True)
    Bathroom = models.IntegerField(blank=True, null=True)
    Property_Description = models.CharField(max_length=500, blank=True, null=True)
    Rate = models.IntegerField( blank=True, null=True)
    SqFeet = models.CharField(max_length=50, blank=True, null=True)
    Photo1 = models.ImageField(upload_to="sellproperties", blank=True, null=True)
    Photo2 = models.ImageField(upload_to="sellproperties", blank=True, null=True)
    Photo3 = models.ImageField(upload_to="sellproperties", blank=True, null=True)
    Username = models.CharField(max_length=50, blank=True, null=True)
    Mobile = models.IntegerField(blank=True, null=True)
    User_Place = models.CharField(max_length=100, blank=True, null=True)
    Profile_Picture = models.ImageField(upload_to="user_image", blank=True, null=True)

class wishlistDB(models.Model):
    Username = models.CharField(max_length=50, blank=True, null=True)
    Propertyplace = models.CharField(max_length=100, blank=True, null=True)
    Address = models.CharField(max_length=100, blank=True, null=True)
    Bedrooms = models.IntegerField(blank=True, null=True)
    Bathrooms = models.IntegerField(blank=True, null=True)
    Price = models.CharField(max_length=50, blank=True, null=True)



class ContactDB(models.Model):
    Contact_Name = models.CharField(max_length=50,blank=True,null=True)
    Email = models.EmailField(max_length=50,blank=True,null=True)
    Subject = models.CharField(max_length=100,blank=True,null=True)
    Message = models.CharField(max_length=500,blank=True,null=True)

class EnquiryDB(models.Model):
    Username = models.CharField(max_length=50, blank=True, null=True)
    Mobile = models.IntegerField(blank=True, null=True)
    Address = models.CharField(max_length=100, blank=True, null=True)
    Mobile_User = models.IntegerField(blank=True, null=True)
    Agent = models.CharField(max_length=200,blank=True,null=True)



class RatingDB(models.Model):
    Username = models.CharField(max_length=50,blank=True,null=True)
    Suggestion = models.CharField(max_length=200,blank=True,null=True)
    Rating = models.IntegerField(blank=True,null=True)

class BookingDB(models.Model):
    Bookingid = models.AutoField(primary_key=True)
    Booking_date = models.DateTimeField(default=timezone.now)
    Username = models.CharField(max_length=50, null=True, blank=True)
    Mobile_User = models.IntegerField(blank=True, null=True)
    Mail = models.EmailField(max_length=50, blank=True, null=True)
    Address = models.CharField(max_length=200, blank=True, null=True)
    Price = models.IntegerField(blank=True,null=True)
    Property_Address = models.CharField(max_length=500,blank=True,null=True)
    Agent_Name = models.CharField(max_length=50, blank=True, null=True)
    Agent_Mobile = models.IntegerField(blank=True, null=True)

class PaymentDB(models.Model):
    Booking_date = models.DateTimeField(default=timezone.now)
    Username = models.CharField(max_length=50, null=True, blank=True)
    Mobile_User = models.IntegerField(blank=True, null=True)
    Mail = models.EmailField(max_length=50, blank=True, null=True)
    Address = models.CharField(max_length=200, blank=True, null=True)
    Price = models.IntegerField(blank=True,null=True)
    Property_Address = models.CharField(max_length=500,blank=True,null=True)
    Agent_Name = models.CharField(max_length=50, blank=True, null=True)
    Agent_Mobile = models.IntegerField(blank=True, null=True)
    Card_number = models.BigIntegerField(null=True,validators=[MinValueValidator(1000000000000000),MaxValueValidator(9999999999999999)])
    Expiry_date = models.CharField(null=True,max_length=5, help_text="Format: MM/YY")
    CVV = models.IntegerField(null=True,validators=[MinValueValidator(100),MaxValueValidator(999)])

class VisitDB(models.Model):
    Name = models.CharField(max_length=50,blank=True,null=True)
    Visit_date = models.DateField()
    Visit_time = models.TimeField()
    Mobile = models.IntegerField(blank=True,null=True)
    Current_date = models.DateTimeField(default=timezone.now)
    Property_Address = models.CharField(max_length=200, blank=True, null=True)



