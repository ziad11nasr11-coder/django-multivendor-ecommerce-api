from django.db import models
from accounts.models import SellerUser
#from categories.models import Category
class Product(models.Model):
    seller = models.ForeignKey(
        SellerUser,
        related_name='products',
        on_delete=models.CASCADE
    )
    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    #category = models.Foreignkey(Category, related_name='products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

