# home/urls.py

from django.urls import path
from . import views  # Import the views module from the home app

urlpatterns = [
    path('', views.home, name='home'),  # Map the root URL to the home view
]