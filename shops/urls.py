# shops/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.shop_dashboard, name='shop-dashboard'),
    path('create/', views.create_shop, name='create-shop'),
]