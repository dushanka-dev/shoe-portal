from django.contrib import admin
from django.urls import path
from . import views
from .views import AddToCart, EditCart

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add/<item_id>/', AddToCart.as_view(), name='add_to_cart'),
    path('edit-cart/<item_id>/', EditCart.as_view(), name='edit_cart'),
]
