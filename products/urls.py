from django.contrib import admin
from django.urls import path
# from . import views
from .views import AllProducts, ProductDetail

urlpatterns = [
    path('allproducts/', AllProducts.as_view(), name='all-products'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    # path('product/', views.products, name='products'),
]
