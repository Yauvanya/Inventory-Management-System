  
from django.db import models

# Create your models here.

class materialClass(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    
class rawMaterials(models.Model): 
    UNITS_CHOICES = [
        (1,"mg"),
        (2,"g"),
        (3,"kg"),
        (4,"ml"),
        (5,"l")
    ]       
    id = models.CharField(primary_key=True)
    material_class = models.ForeignKey(materialClass)
    mat_name = models.CharField(max_length=100,unique=True)
    quantity_present = models.FloatField(max_length=100)
    units = models.CharField(choices=UNITS_CHOICES)

class packagedProducts(models.Model):
    UNITS_CHOICES = [
        (1,"mg"),
        (2,"g"),
        (3,"kg"),
        (4,"ml"),
        (5,"l")
    ]
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100,unique=True)
    ingredient = models.ManytoManyField(rawMaterials)
    quantity_present = models.FloatField()
    units = models.CharField(choices=UNITS_CHOICES)

#seller info and input raw materials




# class ingredeints(models.Model):
#     id = models.AutoField(primary_key=True)
#     RawMatId = models.ForeignKey(packagedProducts)
#     quantity_used = models.CharField()
#     units = models.CharField()



# class materials(models.Model):
#     name = models.

# class packagedProducts(models.Model):

# class shippingProducts(models.Model):
