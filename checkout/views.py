from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.views.generic import View

from .forms import OrderForm

class CheckoutForm(View):
    """Checkout form"""

    def get(self, request):
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart at the moment")
            return redirect(reverse('products'))

        order_form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': 'pk_test_51L4NLsAhQRhfFaYIIkXALsCPRIG1bpYROz2IxgxE9KZDHEMoo2otUuWXFwdQHrYI47FCm5WVOo9NkZVqMky1t5uz009Y90jvcS',
            'client_secret': 'test client secret',
        }

        return render(request, template, context)
