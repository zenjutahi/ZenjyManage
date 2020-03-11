from django.conf import settings
from django.contrib import admin

from .models import Business, BusinessCategory, ProductCategory, Product

# Register your models here.


class BusinessCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(BusinessCategory, BusinessCategoryAdmin)


class BusinessAdmin(admin.ModelAdmin):
    list_display = ['owner', 'business_category', 'name', 'slug',
                    'description', 'address', 'country', 'contact_number', 'city']
    list_filter = ['owner', 'business_category', 'name', 'updated_at']
    list_editable = ['contact_number', 'address', 'name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Business, BusinessAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'product_category', 'discount_price', 'price', 'stock',
                    'available', 'created_at', 'updated_at', 'label']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available', 'discount_price']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
