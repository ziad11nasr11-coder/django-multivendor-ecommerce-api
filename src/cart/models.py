from django.db import models
from accounts.models import User
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        ordering = ["-created_at"]
    def __str__(self):
        return f"Cart #{self.id} - {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"
        ordering = ["-created_at"]
    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
    
    