from django.shortcuts import render, redirect, reverse
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
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            if item_id in list(cart.keys()):
                if size in cart[item_id]['items_by_size'].keys():
                    cart[item_id]['items_by_size'][size] += quantity
                else:
                    cart[item_id]['items_by_size'][size] = quantity
            else:
                cart[item_id] = {'items_by_size': {size: quantity}}
        else:
            if item_id in list(cart.keys()):
                cart[item_id] += quantity
            else:
                cart[item_id] = quantity

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect(redirect_url)


class EditCart(View):
    """ Add products to shopping cart """

    def post(self, request, item_id):
        """ Add a quantity of the product to the cart """

        quantity = int(request.POST.get('quantity'))
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            if quantity > 0:
                cart[item_id]['items_by_size'][size] = quantity
            else:
                del cart[item_id]['items_by_size'][size]
                if not cart[item_id]['items_by_size']:
                    cart.pop(item_id)
        else:
            if quantity > 0:
                cart[item_id] = quantity
            else:
                cart.pop(item_id)

        request.session['cart'] = cart
        return redirect(reverse('cart_view'))

