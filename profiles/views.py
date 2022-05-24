from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView

from .models import UserProfile

# Create your views here.

# def profiles(request):
#     """Display profile"""

#     profile = get_object_or_404(UserProfile, user=request.user)

#     template = 'profiles/profile.html'
#     context = {
#         'profile': profile,
#     }

#     return render(request, template, context)

class Profiles(UpdateView):
    """Display all posts"""

    model = UserProfile
    fields = ['default_phone_number', 'default_street_address1', 'default_street_address2', 'default_town_or_city', 'default_county', 'default_postcode', 'default_country']
    template_name = 'profiles/profile.html'
    success_url = 'profile'

    def get_object(self, queryset=None):
        user_obj = get_object_or_404(UserProfile, user=self.request.user)
        return user_obj

    def form_valid(self, form):
        messages.success(self.request, 'Your Profile Updated Successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile')
