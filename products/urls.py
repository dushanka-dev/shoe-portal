from django.contrib import admin
from django.urls import path
from . import views
from .views import Categories, ProductDetail, AllProducts

urlpatterns = [
    path('products/', AllProducts.as_view(), name='products'),
    path('categories/', Categories.as_view(), name='categories'),
    # path('productcategory/', ProductsCategory.as_view(), name='product-category'),
    path('product-detail/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    # path('products/', views.all_products, name='products'),
]
