from django.db import models
from user.models import KesconUser
from products.models import Product
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(KesconUser, related_name='cart', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Cart of {self.user.username}'

    @property
    def get_cart_total(self):
        total = sum(item.get_total for item in self.items.all())
        return total
        
    @property
    def get_cart_items(self):
        total_items = sum(item.quantity for item in self.items.all())
        return total_items


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} ({self.quantity}) in cart of {self.cart.user.username}'

    @property
    def get_total(self):
        total=self.product.price * self.quantity
        return total