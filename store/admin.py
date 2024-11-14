from django.contrib import admin
from store.models import Product,Category



class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)