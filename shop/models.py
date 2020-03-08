from django.db import models
from django.conf import settings
from accounts.models import CustomUser

# Create your models here.


class ShopCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        app_label = 'shops'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Shop(models.Model):
    owner = models.ForeignKey(
        CustomUser, related_name='my_shops', on_delete=models.CASCADE)
    shop_category = models.ForeignKey(
        ShopCategory,  on_delete=models.DO_NOTHING, related_name='shops')
    shop_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=200, db_index=True)
    logo = models.ImageField(
        upload_to='shop/%Y/%m/%d', blank=True)
    description = models.CharField(max_length=1000, blank=True)
    address = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip = models.CharField(max_length=5, blank=True)
    contact_number = models.CharField(max_length=12, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ('shop_name',)
        app_label = 'shops'

    def __str__(self):
        return "{}".format(self.shop_name)


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    shop = models.ForeignKey(
        Shop, related_name='products', on_delete=models.CASCADE)
    product_category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name='productscategory')
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(
        upload_to='products/%Y/%m/%d', blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=50)
    stock = models.PositiveIntegerField(default=100)
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=100)
    label = models.CharField(max_length=100, blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return "{}".format(self.name)
