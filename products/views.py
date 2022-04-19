from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.

# def products(request):
#     """View to return index page """

#     return render(request, 'products/products.html')


class AllProducts(ListView):
    """List all product to page"""

    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
