# shop_ease/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Include the home app's URLs
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('shops/', include('shops.urls')),
    path('chat/', include('chat.urls')),
    path('login/', include('django.contrib.auth.urls')),  # Default login views
    # Add other URLs here...
]