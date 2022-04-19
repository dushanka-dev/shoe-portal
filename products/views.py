from django.shortcuts import render

# Create your views here.

def products(request):
    """View to return index page """

    return render(request, 'products/products.html')