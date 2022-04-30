from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from django.http import HttpResponseRedirect
# from django.views import View
from django.views.generic import ListView, DetailView
from .models import Category, Product

# Create your views here.


class AllProducts(ListView):
    """List all product to page"""

    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'

class Categories(ListView):
    """List all product categories"""

    model = Category
    template_name = 'products/categories.html'
    context_object_name = 'categories'


class ProductsCategory(ListView):
    """List of all products in a Category"""

    model = Category
    template_name = 'products/product_category_detail.html'
    context_object_name = 'products_in_category'

    # def get_queryset(self):
    #     return Category.objects.all()


class ProductDetail(DetailView):
    """Display individual products on product page"""

    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product_detail'

