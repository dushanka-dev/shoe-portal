from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

# Create your views here.

# def products(request):
#     """View to return index page """

#     return render(request, 'products/product_detail.html')


class AllProducts(ListView):
    """List all product to page"""

    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    """Display individual products on product page"""

    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product_detail'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)




