  
from django.db import models

# Create your models here.
class materialClass(models.Model):
    packaging_materials = models.CharField(max_length=100)
    raw_materials = models.CharField(max_length=100)

class materials(models.Model):
    name = models.

class packagedProducts(models.Model):

class shippingProducts(models.Model):