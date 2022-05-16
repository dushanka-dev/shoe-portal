from django.shortcuts import render

# Create your views here.

def cart_view(request):
    """View to return index page """

    return render(request, 'cart/cart.html')
