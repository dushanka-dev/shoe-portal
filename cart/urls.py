from django.contrib import admin
from django.urls import path
from . import views
from .views import AddToCart

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add/<item_id>/', AddToCart.as_view(), name='add_to_cart'),
]
