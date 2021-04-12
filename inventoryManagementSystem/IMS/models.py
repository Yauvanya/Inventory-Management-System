  
from django.db import models

# Create your models here.
class rawMaterials(models.Model):
    id = models.CharField(primary_key=True)
    mat_name    = models.CharField()
    quantity_present = models.CharField()
    units = models.CharField()


class packagedProducts(models.Model):
    packaged_product_id = models.CharField()
    name = models.TextField()
    quantity_present = models.CharField()

class ingredeints(models.Model):
    RawMatId = models.ForeignKey(packagedProducts)
    quantity_used = models.CharField()
    units = models.CharField()

class packagingMaterials(models.Model):
    packMatId = models.ForeignKey(packagedProducts)
    quantity_used = models.CharField()
    units = models.CharField()
class materialClass(models.Model):
    packaging_materials = models.CharField(max_length=100)
    raw_materials = models.CharField(max_length=100)

class materials(models.Model):
    name = models.

class packagedProducts(models.Model):

class shippingProducts(models.Model):
