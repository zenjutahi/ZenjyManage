from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.business_list, name='business_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.business_list, name='business_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)$', views.business_detail, name='business_detail'),
]
