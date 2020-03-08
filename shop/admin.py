from django.conf import settings
from django.contrib import admin

from .models import Shop, ShopCategory, ProductCategory, Product

# Register your models here.


class ShopCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ShopCategory, ShopCategoryAdmin)


class ShopAdmin(admin.ModelAdmin):
    list_display = ['owner', 'shop_category', 'shop_name', 'slug', 'logo',
                    'description', 'address', 'country', 'contact_number', 'city']
    list_filter = ['owner', 'shop_category', 'shop_name', 'updated_at']
    list_editable = ['contact_number', 'address', 'shop_name']
    prepopulated_fields = {'slug': ('shop_name',)}


admin.site.register(Shop, ShopAdmin)


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
