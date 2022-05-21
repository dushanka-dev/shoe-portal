from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.


def cart_view(request):
    """View to return index page """

    return render(request, 'cart/cart.html')


class AddToCart(View):
    """ Add products to shopping cart """

    def post(self, request, item_id):
        """ Add a quantity of the product to the cart """

        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        cart = request.session.get('cart', {})

        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect(redirect_url)