from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    Category_Name = models.CharField(max_length=50,blank=True,null=True)
    Description = models.CharField(max_length=50,blank=True,null=True)
    Image = models.ImageField(upload_to="categories",blank=True,null=True)

class ProductDB(models.Model):
    Category_Name = models.CharField(max_length=50, blank=True, null=True)
    Propertyplace = models.CharField(max_length=100,blank=True,null=True)
    Address = models.CharField(max_length=1000,blank=True,null=True)
    Bedrooms = models.IntegerField(blank=True,null=True)
    Bathrooms = models.IntegerField(blank=True,null=True)
    Description = models.CharField(max_length=5000, blank=True, null=True)
    Price = models.IntegerField(blank=True, null=True)
    Sqfeet = models.CharField(max_length=50, blank=True, null=True)
    Image1 = models.ImageField(upload_to="properties",blank=True,null=True)
    Image2 = models.ImageField(upload_to="properties",blank=True,null=True)
    Image3 = models.ImageField(upload_to="properties",blank=True,null=True)
    Agent_Name = models.CharField(max_length=50, blank=True, null=True)
    Designation = models.CharField(max_length=50, blank=True, null=True)
    Mobile = models.IntegerField(blank=True, null=True)
    Agent_Place = models.CharField(max_length=100, blank=True, null=True)
    Profile = models.ImageField(upload_to="agent", blank=True, null=True)
    Googlemap = models.CharField(max_length=1000,blank=True,null=True)

class MembersDB(models.Model):
    Name = models.CharField(max_length=50,blank=True,null=True)
    Role = models.CharField(max_length=50,blank=True,null=True)
    Image = models.ImageField(upload_to="members",blank=True,null=True)