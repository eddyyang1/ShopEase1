# shops/views.py

from django.shortcuts import render, redirect
from .models import Shop
from django.contrib.auth.decorators import login_required


@login_required
def shop_dashboard(request):
    if not request.user.is_seller:
        return redirect('home')  # Only allow sellers to manage shops

    # Check if the seller already has a shop
    shop = Shop.objects.filter(owner=request.user).first()

    if not shop:
        # If no shop exists, redirect to create a shop page
        return redirect('create-shop')

    return render(request, 'shop_dashboard.html', {'shop': shop})


@login_required
def create_shop(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        location = request.POST.get('location')

        # Create a new shop for the seller
        Shop.objects.create(owner=request.user, name=name, description=description, location=location)
        return redirect('shop-dashboard')

    return render(request, 'create_shop.html')