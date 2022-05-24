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

def profiles(request):
    """Display profile"""

    template = 'profiles/profile.html'
    context = {

    }

    return render(request, template, context)


# class Profiles(DetailView):
#     """Display profile"""

#     model = UserProfile
#     template_name = 'profiles/profile.html'
#     pk_url_kwarg = 'pk'
#     # template_name_field = 'profile'
