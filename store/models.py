from django.db import models
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products/', blank=True, null=True) 
    sold_quantity = models.PositiveIntegerField(default=0)  # Total sold quantity

    def __str__(self):
        return self.name

    def is_in_stock(self):
        return self.stock > 0

    def available_quantity(self):
        return self.stock - self.sold_quantity
    
    is_featured = models.BooleanField(default=False)
    
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True) 
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

   

    def __str__(self):
        return self.name