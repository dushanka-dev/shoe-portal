from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.generic import View
from django.contrib import messages

from products.models import Product

# Create your views here.


def cart_view(request):
    """View to return index page """

    return render(request, 'cart/cart.html')


class AddToCart(View):
    """ Add products to shopping cart """

    def post(self, request, item_id):
        """ Add a quantity of the product to the cart """

        product = Product.objects.get(pk=item_id)
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

        messages.success(request, f'Added {product.name} to your bag')
        request.session['cart'] = cart
        return redirect(redirect_url)


class EditCart(View):
    """ Add products to shopping cart """

    def post(self, request, item_id):
        """ Add a quantity of the product to the cart """

        product = Product.objects.get(pk=item_id)
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

        messages.success(request, f'Updated {product.name} quantity!')
        request.session['cart'] = cart
        return redirect(reverse('cart_view'))


class RemoveFromCart(View):
    """ Remove items from cart"""

    def post(self, request, item_id):
        """Remove the item from the shopping bag"""

        product = Product.objects.get(pk=item_id)

        try:
            size = None
            if 'product_size' in request.POST:
                size = request.POST['product_size']
            cart = request.session.get('cart', {})

            if size:
                del cart[item_id]['items_by_size'][size]
                if not cart[item_id]['items_by_size']:
                    cart.pop(item_id)
            else:
                cart.pop(item_id)

            messages.success(request, f'Removed {product.name} from your shopping cart')
            request.session['cart'] = cart
            return HttpResponse(status=200)

        except Exception as e:
            return HttpResponse(status=500)
