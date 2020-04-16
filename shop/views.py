from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from .models import BusinessCategory, Business, ProductCategory, Product





def product_list(request, category_slug=None):
    product_category = None
    product_categories = ProductCategory.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        product_category = get_object_or_404(Product, slug=category_slug)
        print(product_category)
        products = products.filter(business_category=product_category)
    return render(
        request,
        'shop/home/product_list.html',
        {'product_category': product_category,
         'product_categories': product_categories,
         'products': products })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product':product},
                  {'cart_product_form': cart_product_form})


def checkout_page(request):
    product_categories = ProductCategory.objects.all()
    products = Product.objects.filter(available=True)
    return render(
        request,
        'shop/home/checkout_page.html',
        {'product_categories': product_categories,
         'products': products })

def business_list(request, category_slug=None):
    busines_category = None
    busines_categories = BusinessCategory.objects.all()
    businesses = Business.objects.filter(is_active=True)
    if category_slug:
        busines_category = get_object_or_404(Business, slug=category_slug)
        businesses = businesses.filter(business_category=busines_category)
    return render(
        request,
        'shop/business/list.html',
        {'busines_category': busines_category,
         'busines_categories': busines_categories,
         'businesses': businesses })


def business_detail(request, id, slug):
    business = get_object_or_404(Business,
                                 id=id,
                                 slug=slug,
                                 is_active=True)
    return render(request,
                  'shop/business/detail',
                  {'business': business})
