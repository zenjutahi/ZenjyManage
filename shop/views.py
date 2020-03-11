from django.shortcuts import render, get_object_or_404
from .models import BusinessCategory, Business


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
