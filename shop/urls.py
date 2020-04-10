from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    re_path(r'^$', views.product_list, name='product_list'),
    path('checkout/', views.checkout_page, name='checkout_page'),
    re_path(r'^dashboard/$', views.business_list, name='business_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.business_list, name='business_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)$', views.business_detail, name='business_detail'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
						document_root=settings.MEDIA_ROOT)
