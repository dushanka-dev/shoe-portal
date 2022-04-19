from django.contrib import admin
from django.urls import path
# from . import views
from .views import AllProducts

urlpatterns = [
    path('allproducts/', AllProducts.as_view(), name='all-products')
]
