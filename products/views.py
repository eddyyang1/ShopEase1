# products/views.py

from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


def product_list(request):
    # Display a list of all available products
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


@login_required
def add_product(request):
    # Allow sellers to add a new product to their shop
    if not request.user.is_seller:
        return redirect('home')  # Only allow sellers to add products

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user  # Associate the product with the logged-in seller
            product.save()
            return redirect('seller-dashboard')  # Redirect to the seller dashboard after saving
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})
