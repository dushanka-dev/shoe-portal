from django.contrib import admin
from django.urls import path
from . import views
from .views import Profiles, UserOrdersView

urlpatterns = [
    # path('usersprofile/', views.profiles, name='profile'),
    path('profile/', Profiles.as_view(), name='profile'),
    path('order-history/<order_number>', UserOrdersView.as_view(), name='order-history'),
]
