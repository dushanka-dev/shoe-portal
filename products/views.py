from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, View
from .models import Category, Product

# Create your views here.

class AllProducts(View):
     """List all product categories"""

     def get(self, request):
        """List all product categories"""

        products = Product.objects.all().order_by('name')
        category = None

        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            products = products.filter(category__name__in=category)
            category = Category.objects.filter(name__in=category)

        context = {
            'products': products,
            'active_category': category,
        }

        return render(request, 'products/products.html', context)

class Categories(ListView):
    """List all product categories"""

    model = Category
    template_name = 'products/categories.html'
    context_object_name = 'categories'


class ProductDetail(DetailView):
    """Display products details on product page"""

    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product_detail'

