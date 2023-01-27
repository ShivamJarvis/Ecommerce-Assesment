from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    rating = models.FloatField(default=5)
    image = models.ImageField(upload_to="product/images/",null=True,blank=True)
    price = models.FloatField(default=0)
    seller = models.CharField(max_length=255)
    brand = models.CharField(max_length=120)
    stock = models.IntegerField(default=0)
    is_cod = models.BooleanField(default=True)
    is_express = models.BooleanField(default=True)
    is_fragile = models.BooleanField(default=False)
    cod_charges = models.FloatField(default=0)
    express_charges = models.FloatField(default=0)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    min_qty_to_buy = models.IntegerField(default=1)
    max_qty_to_buy = models.IntegerField(default=1)
    standard_charges = models.IntegerField(default=50)
    description = models.TextField(null=True,blank=True)
    specification = models.TextField(null=True,blank=True)
    is_popular = models.BooleanField(default=False)
    launch_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-launch_date',)
    def __str__(self):
        return f'{self.id}. {self.name}'
