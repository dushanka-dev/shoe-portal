from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.views.generic import View
from django.conf import settings

import stripe

from cart.contexts import cart_content
from products.models import Product
from .models import Order, OrderLineItem
from .forms import OrderForm


class CheckoutForm(View):
    """Checkout form"""

    def post(self, request):

        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'customer_email': request.POST['customer_email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('cart_view'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        
        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

        current_cart = cart_content(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )


        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


    def get(self, request):

        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart at the moment")
            return redirect(reverse('products'))

        current_cart = cart_content(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


class CheckoutSuccess(View):
    """Checkout success page view"""

    def get(self, request, order_number):
        """
        Handle successful checkouts
        """
        save_info = request.session.get('save_info')
        order = get_object_or_404(Order, order_number=order_number)
        messages.success(request, f'Order successfully processed! \
            Your order number is {order_number}. A confirmation \
            email will be sent to {order.customer_email}.')

        if 'cart' in request.session:
            del request.session['cart']

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
        }

        return render(request, template, context)
