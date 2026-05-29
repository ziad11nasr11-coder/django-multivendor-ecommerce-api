from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    class UserType(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        SELLER = 'seller', 'Seller'
        CUSTOMER = 'customer', 'Customer'

    user_type = models.CharField(max_length=10, choices=UserType.choices, default=UserType.CUSTOMER)
    

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "users"
        ordering = ["date_joined"]

    def __str__(self):
        return self.username
    
class ProfileBase(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="%(class)s_profile")
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
        


class AdminProfile(ProfileBase):
    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"
class CustomerProfile(ProfileBase):
    address = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

class SellerProfile(ProfileBase):
    store_name = models.CharField(max_length=100, blank=True, null=True)
    store_description = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"

class AdminUser(User):
    class Meta:
        proxy = True
        verbose_name = "Admin Users"
        verbose_name_plural = "Admin Users"


class SellerUser(User):
    class Meta:
        proxy = True
        verbose_name = "Seller Users"
        verbose_name_plural = "Seller Users"


class CustomerUser(User):
    class Meta:
        proxy = True
        verbose_name = "Customer Users"
        verbose_name_plural = "Customer Users"
