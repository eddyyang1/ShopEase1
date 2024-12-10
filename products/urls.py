# products/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_product, name='add-product'),
    path('list/', views.product_list, name='product-list'),
]