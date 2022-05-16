from django.shortcuts import render
from django.db.models import Q
# from django.shortcuts import get_object_or_404
# from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, View
from .models import Category, Product

# Create your views here.

class AllProducts(View):
    """Products view to retrieve and filter products and categories"""

    def get(self, request):
        """Get product objects, order them alphabetically.
           Get category, split by commas. Filter products and category.
        """

        products = Product.objects.all().order_by('name')
        category = None
        sort = None
        direction = None

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'sort':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            products = products.filter(category__name__in=category)
            category = Category.objects.filter(name__in=category)

        current_sorting = f'{sort}_{direction}'

        context = {
            'products': products,
            'active_category': category,
            'current_sorting': current_sorting,
        }

        return render(request, 'products/products.html', context)


class SearchResults(ListView):
    """List all search results"""

    model = Product
    template_name = 'products/search.html'
    context_object_name = 'search_queries'

    def get_queryset(self):
        """List all search results"""
        query = self.request.GET.get("q")
        search_queries = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return search_queries


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

