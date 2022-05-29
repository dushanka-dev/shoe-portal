from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView

from checkout.models import Order
from .models import UserProfile
from .forms import ProfileForm

# Create your views here.

# def profiles(request):
#     """Display profile"""

#     profile = get_object_or_404(UserProfile, user=request.user)

#     template = 'profiles/profile.html'
#     context = {
#         'profile': profile,
#     }

#     return render(request, template, context)


class Profiles(View):
    """Display all posts"""

    def get(self, request):
        """ Display the user's profile. """
        profile = get_object_or_404(UserProfile, user=request.user)

        if request.method == 'POST':
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully')

        form = ProfileForm(instance=profile)
        orders = profile.orders.all()

        template = 'profiles/profile.html'
        context = {
            'form': form,
            'orders': orders,
            'on_profile_page': True
        }

        return render(request, template, context)


class UserOrdersView(View):
    """Users all orders"""

    def get(self, request, order_number):
        """ Display the user's profile. """

        order = get_object_or_404(Order, order_number=order_number)

        messages.info(request, (
            f'This is a past confirmation for order number {order_number}. '
            'A confirmation email was sent on the order date.'
        ))

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
            'from_profile': True,
        }

        return render(request, template, context)