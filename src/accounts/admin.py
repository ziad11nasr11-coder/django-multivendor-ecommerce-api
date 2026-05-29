from django.contrib import admin
from .models import (
    User,
    AdminUser,
    SellerUser,
    CustomerUser,
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "user_type"]

# Admin Users
@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):

    list_display = ["username", "email"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user_type="admin")


# Seller Users
@admin.register(SellerUser)
class SellerUserAdmin(admin.ModelAdmin):

    list_display = ["username", "email"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user_type="seller")


# Customer Users
@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):

    list_display = ["username", "email"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user_type="customer")