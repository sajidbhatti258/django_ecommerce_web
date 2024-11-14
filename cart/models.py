from django.db import models

from  django.conf import settings

from store.models import Product


# Create your models here.
class Cart(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete= models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        
        return f'Cart for user {self.user.username}'
    

class CartItem(models.Model):
    
    cart = models.ForeignKey(Cart, related_name='items' , on_delete=models.CASCADE)
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    quantity = models.PositiveIntegerField()
    
    class Meta:
        
        unique_together = ['cart', 'product']
        
    def __str__(self):
        
        return f'Cart Item for product {self.product.name}, in cart {self.cart.id}'